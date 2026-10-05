"""Chat EOT/EOS, raw decoding and provided versus generated dialogue histories."""
import re
import torch
from jmicro.japanese_evaluation import repetition_metrics
from jmicro.tokenizer import SUPPRESS_IDS
from jmicro.training import autocast,isolated_evaluation


def decode_reply(tokenizer,ids):
    if 1 in ids:
        return dict(text="",valid_utf8=False,raw_bytes_hex=None,decode_error="unknown-token-id1")
    raw = tokenizer.decode_bytes(ids)
    try: text,valid = raw.decode("utf-8"),True
    except UnicodeDecodeError: text,valid = raw.decode("utf-8",errors="replace"),False
    return dict(text=text,valid_utf8=valid,raw_bytes_hex=raw.hex(),decode_error=None if valid else "invalid-utf8")


def generate_reply(model,tokenizer,messages,device="cpu",dtype="fp32",max_new=64,suppressed=True,check=lambda:None):
    context = model.config["max_position_embeddings"]
    if type(max_new) is not int or not 0 < max_new < context:
        raise ValueError("Positive generation budget must fit model context")
    prompt,removed = tokenizer.chat_prompt(messages,context-max_new)
    ids = [];cache = None;current = torch.tensor([prompt],device=device)
    reason = "max_new_tokens"
    with isolated_evaluation(model):
        for _ in range(max_new):
            check()
            with autocast(device,dtype): output = model(current,cache=cache,use_cache=True)
            cache = output.cache;scores = output.logits[0,-1].float().clone()
            if not torch.isfinite(scores).all(): raise ValueError("Nonfinite Chat generation logits")
            if suppressed: scores[list(SUPPRESS_IDS)] = -torch.inf
            token = int(scores.argmax());ids.append(token)
            if token in (7,3):
                reason = "eot" if token == 7 else "eos";break
            current = torch.tensor([[token]],device=device)
    decoded = decode_reply(tokenizer,ids)
    row = dict(**decoded,generated_ids=ids,generated_tokens=len(ids),stop_reason=reason,
        role_leak=any(token in (4,5,6) for token in ids),unexpected_special=any(token in (0,1,2,4,5,6) for token in ids),
        empty_response=not decoded["text"].strip(),suppressed=suppressed,suppressed_ids=list(SUPPRESS_IDS) if suppressed else [],
        decoding="greedy",prompt_ids=prompt,prompt_tokens=len(prompt),removed_turns=removed,
        full_history_retained=removed == 0,user_turns=sum(m["role"] == "user" for m in messages),max_new_tokens=max_new)
    metrics = repetition_metrics(dict(row,stop_reason="stop_id" if reason in ("eot","eos") else reason))
    row["repetition"] = bool(re.search(r"(.{2,}?)\1\1",row["text"],re.DOTALL))
    row["repeat_metrics"] = {k:metrics[k] for k in ("char_4gram_repeat","token_4gram_repeat","same_sentence_reappears","first_adjacent_triple_repeat_char")}
    return row


def rollout_dialogue(model,tokenizer,case,device="cpu",dtype="fp32",max_new=64,check=lambda:None):
    messages = case["messages"]
    if not messages or messages[-1]["role"] != "user": raise ValueError("Dev case must end in user")
    history = [dict(messages[0])] if messages[0]["role"] == "system" else []
    replies = []
    for message in messages:
        if message["role"] != "user": continue
        history.append(dict(message))
        row = generate_reply(model,tokenizer,history,device,dtype,max_new,True,check)
        row.update(id=case["id"],turn=len(replies)+1,history_mode="model_generated_assistant_history")
        replies.append(row)
        # Match a text-based client: serialize decoded body as the next
        # Assistant turn. Every original ID/error remains in the raw rows.
        history.append(dict(role="assistant",content=row["text"]))
    return dict(id=case["id"],family_id=case["family_id"],category=case["category"],split=case["split"],
        checks=case["checks"],user_turns=len(replies),replies=replies,
        history_policy="Generated decoded body text; all raw token IDs, role/UTF8 errors and failed earlier turns retained separately",
        full_history_retained=all(r["full_history_retained"] for r in replies))


def summarize_chat(rows):
    if not rows: raise ValueError("Nonempty Chat output rows required")
    count = len(rows)
    counters = dict(outputs=count,stop=sum(r["stop_reason"] in ("eot","eos") for r in rows),
        EOT=sum(r["stop_reason"] == "eot" for r in rows),EOS=sum(r["stop_reason"] == "eos" for r in rows),
        empty=sum(r["empty_response"] for r in rows),role_leak=sum(r["role_leak"] for r in rows),
        unicode_failure=sum(not r["valid_utf8"] for r in rows),repetition=sum(r["repetition"] for r in rows),
        trimmed_history=sum(not r["full_history_retained"] for r in rows))
    counters["fractions"] = {k:counters[k]/count for k in ("stop","empty","role_leak","unicode_failure","repetition")}
    counters["mechanical_checks_only"] = dict(stop_at_least95=counters["stop"]/count >= .95,
        empty_at_most5=counters["empty"]/count <= .05,role_leak_at_most1=counters["role_leak"]/count <= .01,
        raw_unicode0=counters["unicode_failure"] == 0,full_fixed_history=counters["trimmed_history"] == 0)
    counters["grammar_relevance_context_not_scored"] = True
    return counters
