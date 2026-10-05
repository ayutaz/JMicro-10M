"""Train-only, bounded gradient/probability diagnosis; no optimizer exists."""
import argparse
from collections import Counter
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.eos_pilot import TrainView
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,autocast,configure_compile_cache,rng_state,restore_rng
from jmicro.sequence_unlikelihood import greedy_rollout,continuation_logits,repeated_ngram_mask,sequence_unlikelihood_sum
from phase6_performance import alive,identity,finite_state
from sequence_objective_trainer import train_prefixes
from run_eos_short_pilot import equal_state
from run_sequence_objective_comparison import RUN as STUDY,CONFIG as STUDY_CONFIG,preflight as study_preflight

CONFIG=ROOT/"configs/phase6/sequence_objective_diagnostic.json"
RUN=ROOT/"reports/phase6/sequence-objective-diagnostic-20261006"
BLOCKED=(0,1,2,4,5,6,7)
SOURCES=("scripts/diagnose_sequence_objective.py","scripts/diagnose_sequence_objective.ps1",
         "scripts/sequence_objective_trainer.py","src/jmicro/sequence_unlikelihood.py")


def reference(path):return dict(path=str(path),sha256=sha256(path))


def gradient_summary(ce,ul):
    if set(ce)!=set(ul) or any(ce[k].shape!=ul[k].shape for k in ce):
        raise ValueError("Gradient parameter identity/shape differs")
    a=torch.cat([ce[k].detach().reshape(-1) for k in ce]).double()
    b=torch.cat([ul[k].detach().reshape(-1) for k in ce]).double()
    assert bool(torch.isfinite(a).all()) and bool(torch.isfinite(b).all())
    aa=float(a.dot(a));bb=float(b.dot(b));dot=float(a.dot(b));an=math.sqrt(aa);bn=math.sqrt(bb)
    result=dict(CE_norm=an,UL_norm=bn,UL_to_CE_norm=bn/an if an else None,
                cosine=dot/(an*bn) if an and bn else None,alpha_combinations={})
    for alpha in (0.,.01,.1):
        combined=math.sqrt(max(0.,aa+2*alpha*dot+alpha*alpha*bb))
        result["alpha_combinations"][str(alpha)]=dict(weighted_UL_to_CE_norm=alpha*bn/an if an else None,
            combined_norm_before_clip=combined,combined_cosine_to_CE=(aa+alpha*dot)/(combined*an) if combined and an else None)
    return result


def probability_summary(logits,ids,negative):
    valid=ids.ne(0);assert bool(valid.any()) and negative.shape==ids.shape
    scores=logits.detach().float();p=scores.softmax(-1);blocked=p[...,list(BLOCKED)].sum(-1)
    raw=p.gather(-1,ids[...,None]).squeeze(-1)
    allowed=scores.clone();allowed[...,list(BLOCKED)]=-torch.inf
    conditional=allowed.softmax(-1).gather(-1,ids[...,None]).squeeze(-1)
    mean=lambda v,m:float(v[m].mean()) if bool(m.any()) else None
    argmax=scores.argmax(-1);raw_blocked=torch.zeros_like(valid)
    for token in BLOCKED:raw_blocked|=argmax.eq(token)
    return dict(blocked_probability_mean=mean(blocked,valid),blocked_probability_max=float(blocked[valid].max()),
        blocked_probability_at_negative_mean=mean(blocked,negative),raw_argmax_blocked_fraction=mean(raw_blocked.float(),valid),
        raw_generated_probability_mean=mean(raw,valid),conditional_generated_probability_mean=mean(conditional,valid),
        raw_negative_probability_mean=mean(raw,negative),conditional_negative_probability_mean=mean(conditional,negative))


def fixed_inputs(pool):
    view=TrainView(pool["pool"],pool["manifest_sha256"])
    # A predeclared contiguous train window; no huge document index is read.
    chunk=np.array(view.tokens[:32*1024+1],dtype=np.int64)
    x=torch.from_numpy(chunk[:-1].copy().reshape(32,1024))
    y=torch.from_numpy(chunk[1:].copy().reshape(32,1024));y[y.eq(0)|y.eq(2)]=-100
    assert not bool(x.eq(0).any())
    prefixes=train_prefixes([(x,y,0)],8,32);assert prefixes is not None and prefixes.shape==(8,32)
    digest=hashlib.sha256(x.numpy().astype("<i8").tobytes()+y.numpy().astype("<i8").tobytes()).hexdigest()
    return x,y,prefixes,dict(selection="first contiguous32x1024 accepted train tokens; first8 complete BOS heads with32 token prefix",
        token_offset=0,x_y_sha256=digest,prefix_sha256=hashlib.sha256(prefixes.numpy().astype("<i8").tobytes()).hexdigest(),
        valid_input_tokens=x.numel(),scored_CE_targets=int(y.ne(-100).sum()),index_rescanned=False,
        representative_corpus_claim=False)


def contract():
    c,base,parent=study_preflight(STUDY_CONFIG);job=read_json(STUDY/"job.json");result=read_json(STUDY/"compare-result.json")
    review=read_json(STUDY/"review.json")
    assert job["status"]=="complete" and not alive(job) and result["scientific_teacher_tokens"]==50000000
    assert review["status"]=="matched_CE_sequence_UL_learning_and_all160_content_evidence_complete"
    assert review["result_sha256"]==sha256(STUDY/"compare-result.json") and not review["objective_comparison"]["passed"]
    assert not any(v["absolute_screen_pass"] for v in review["practical"].values())
    refs=dict(parent=c["parent"],**{a:dict(path=d["checkpoint"],sha256=d["checkpoint_sha256"])
                                    for a,d in result["checkpoints"].items()})
    return c,base,refs


def inspect():
    c=read_json(CONFIG);study,base,refs=contract()
    assert c["study_config"]==reference(STUDY_CONFIG) and c["study_review"]==reference(STUDY/"review.json")
    assert c["checkpoints"]==refs and c["pool"]==study["pool"] and c["GPU_budget_seconds"]==60
    assert c["implementation"]==implementation_hashes() and c["source_sha256"]=={p:sha256(ROOT/p) for p in SOURCES}
    assert c["optimizer_updates"]==c["scientific_teacher_tokens"]==0 and not c["protected_test_used"]
    x,y,prefixes,summary=fixed_inputs(c["pool"]);assert c["inputs"]==summary
    if (RUN/"job.json").exists() and alive(read_json(RUN/"job.json")):raise ValueError("Actual diagnostic is live; do not duplicate")
    return c,base,x,y,prefixes


def prepare():
    if CONFIG.exists():inspect();return
    study,base,refs=contract();_,_,_,summary=fixed_inputs(study["pool"])
    c=dict(kind="train-only-no-update-gradient-diagnosis",study_config=reference(STUDY_CONFIG),study_review=reference(STUDY/"review.json"),
        checkpoints=refs,pool=study["pool"],inputs=summary,alphas=[0.,.01,.1],GPU_budget_seconds=60,
        CE_path="actual BF16 compiled Flash32x1024 fast training forward",UL_path="native BF16 math cached8x32prefix/max64 continuation",
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        tokenizer=base["tokenizer"],tokenizer_sha256=base["tokenizer_sha256"],
        optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,Base_adopted=False,
        completion="all3 actual checkpoints/same fixed train inputs; finite losses/gradients; norms/cosine/per-layer ratios/special mass/negative token units; exact parameter preservation; actual GPU<=60s")
    atomic_json(CONFIG,c);print("Train-only diagnostic frozen; no GPU started")


def run():
    c,base,x,y,prefixes=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/"job.json"
    old=read_json(jp) if jp.exists() else {}
    if old:
        assert old["config_sha256"]==sha256(CONFIG) and not alive(old)
        if old["status"]=="complete":print("Completed diagnostic retained");return
    prior=old.get("gpu_elapsed_seconds",0.);started=[None];stopped=[False]
    progress=read_json(RUN/"progress.json") if (RUN/"progress.json").exists() else {}
    job=dict(status="running",**identity(),config_sha256=sha256(CONFIG),started_at=old.get("started_at",now()),
             gpu_elapsed_seconds=prior,optimizer_updates=0,scientific_teacher_tokens=0,
             restart_command="scripts/diagnose_sequence_objective.ps1 -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError("Completed diagnostic sections retained")
        if started[0] is not None and prior+time.monotonic()-started[0]>60:raise TimeoutError("Cumulative diagnostic60s exhausted")
    def heartbeat(stage):
        check();job.update(stage=stage,heartbeat_at=now())
        if started[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/"source"/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        assert sha256(ROOT/c["tokenizer"])==c["tokenizer_sha256"];tok=Tokenizer(ROOT/c["tokenizer"])
        atomic_json(RUN/"inputs.json",dict(summary=c["inputs"],prefixes=prefixes.tolist(),prefix_text=[tok.decode(row[1:],errors="replace") for row in prefixes.tolist()],
            fragment_display="Token-boundary prefixes/fragments may split UTF8; replacement display is not an output Unicode failure"))
        with gpu_lock("cuda"):
            started[0]=time.monotonic()
            for name,ref in c["checkpoints"].items():
                if name in progress:continue
                heartbeat(name+"-load");assert sha256(Path(ref["path"]))==ref["sha256"]
                state=torch.load(ref["path"],map_location="cpu",weights_only=False);assert finite_state(state)
                before=rng_state();model=JMicroModel(state["model_config"]).to("cuda");model.load_state_dict(state["model"],strict=True);model.train()
                spec=state["spec"];assert spec["dtype"]=="bf16" and spec["backend"]=="flash" and spec["compile"] and spec["training_fast_path"]
                configure_compile_cache(spec);options=dict(fullgraph=True,dynamic=False)
                if spec.get("compile_mode"):options["mode"]=spec["compile_mode"]
                forward=torch.compile(model,**options);torch.compiler.cudagraph_mark_step_begin()
                heartbeat(name+"-CE-gradient")
                with sdpa_kernel([SDPBackend.FLASH_ATTENTION]),autocast("cuda","bf16"):
                    logits=forward(x.to("cuda"),training_fast_path=True).logits
                    ce_loss=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),y.to("cuda").reshape(-1),ignore_index=-100,reduction="sum")/c["inputs"]["scored_CE_targets"]
                ce_loss.backward();CE=float(ce_loss.detach());ce={n:p.grad.detach().clone() for n,p in model.named_parameters()}
                del logits,ce_loss;model.zero_grad(set_to_none=True);heartbeat(name+"-UL-gradient")
                with sdpa_kernel([SDPBackend.MATH]),autocast("cuda","bf16"):
                    generated=greedy_rollout(model,prefixes.to("cuda"),max_new_tokens=64)
                    negative=torch.tensor(repeated_ngram_mask(generated.tolist()),device="cuda",dtype=torch.bool)
                    scored=continuation_logits(model,prefixes.to("cuda"),generated)
                    ul_loss=sequence_unlikelihood_sum(scored,generated,negative)/max(1,int(generated.ge(8).sum()))
                probs=probability_summary(scored,generated,negative);UL=float(ul_loss.detach());ul_loss.backward()
                ul={n:p.grad.detach().clone() if p.grad is not None else torch.zeros_like(p) for n,p in model.named_parameters()}
                summary=gradient_summary(ce,ul);assert summary["CE_norm"]>0 and math.isfinite(CE) and math.isfinite(UL)
                groups={}
                for n in ce:
                    group="layer-"+n.split(".layers.")[1].split(".")[0] if ".layers." in n else n
                    groups.setdefault(group,[]).append(n)
                layers={g:gradient_summary({n:ce[n] for n in keys},{n:ul[n] for n in keys}) for g,keys in groups.items()}
                ids=generated.tolist();masks=negative.tolist();counts=Counter(t for row,mask in zip(ids,masks,strict=True) for t,m in zip(row,mask,strict=True) if m)
                top=[dict(id=t,positions=n,bytes_hex=tok.decode_bytes([t]).hex(),decoded_fragment=tok.decode([t],errors="replace")) for t,n in counts.most_common(32)]
                unchanged=all(torch.equal(value.detach().cpu(),state["model"][n]) for n,value in model.state_dict().items())
                assert unchanged;restore_rng(before);assert equal_state(before,rng_state());torch.cuda.synchronize()
                progress[name]=dict(checkpoint=ref,update=state["update"],supervised_tokens=state["supervised_tokens"],
                    CE_loss=CE,UL_loss=UL,gradients=summary,parameter_groups=layers,probabilities=probs,
                    generated_body_tokens=int(generated.ge(8).sum()),generated_EOS=int(generated.eq(3).sum()),negative_positions=int(negative.sum()),
                    top_negative_token_fragments=top,outputs=[dict(prefix=p,generated_ids=r,negative_mask=m,text=tok.decode(r,errors="replace"))
                        for p,r,m in zip(prefixes.tolist(),ids,masks,strict=True)],
                    exact_parameters_unchanged=True,RNG_restored=True,optimizer_updates=0,scientific_teacher_tokens=0)
                atomic_json(RUN/"progress.json",progress);del model,forward,state,ce,ul,generated,negative,scored,ul_loss
                gc.collect();torch.cuda.empty_cache();heartbeat(name+"-complete")
            assert set(progress)==set(c["checkpoints"])
            heartbeat("complete")
            atomic_json(RUN/"result.json",dict(status="actual_train_only_gradient_diagnosis_complete",config_sha256=sha256(CONFIG),
                checkpoints=progress,inputs=c["inputs"],optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
                Base_adopted=False,quality_evaluation=False,limitations="One fixed accepted train window, not whole-corpus causality or independent model quality",created_at=now()))
            job.update(status="complete",completed_at=now())
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:
        if started[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument("--prepare",action="store_true");g.add_argument("--inspect",action="store_true")
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect()
    else:run()
