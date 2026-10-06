"""Same complete source stream, only a fresh nonlinear readout Adam is used."""
import copy
from pathlib import Path
import torch
from jmicro.experiment import sha256
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer
from condition_positive_trainer import ConditionPositiveTrainer
from readout_adapter_model import ReadoutAdapterModel,POLICY

KIND='frozen_decoder_nonlinear_readout_Base_full100M_v1'
READOUT_LR=.0001


class ReadoutAdapterTrainer(ParameterAnchorTrainer):
    def __init__(self,parent,pool,original,positive,goals,binding,device='cuda',context=1024,batch=32):
        super().__init__(parent,pool,original,positive,goals,binding,0.,device,context,batch)
        self.model=ReadoutAdapterModel.from_native(self.model)
        options=parent['optimizer']['param_groups'][1]
        self.optimizer=torch.optim.AdamW((self.model.lm_head.down,self.model.lm_head.up),
            lr=READOUT_LR,betas=options['betas'],eps=options['eps'],weight_decay=0.,fused=device=='cuda')
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        self.spec.update(research_kind=KIND,lr=READOUT_LR,weight_decay=0.,readout_adapter=copy.deepcopy(POLICY),
            readout_model_sha256=sha256(Path(__file__).with_name('readout_adapter_model.py')),
            readout_trainer_sha256=sha256(Path(__file__)),
            native_unique_parameters=sum(p.numel() for p in self.model.parameters() if not p.requires_grad),
            new_readout_parameters=sum(p.numel() for p in self.model.parameters() if p.requires_grad))
        self.lineage.update(kind=KIND,native_optimizer_policy='not_used_native_weights_frozen',
            optimizer_policy='fresh_readout_only',scheduler_policy='fresh_constant_readout_LR',
            parent_native_model_config=copy.deepcopy(parent['model_config']),readout_adapter=copy.deepcopy(POLICY))
        self.forward=torch.compile(self.model,fullgraph=True,dynamic=False,mode=self.spec['compile_mode']) if self.spec['compile'] else self.model

    def step(self):
        row=ConditionPositiveTrainer.step(self)
        if (len(self.optimizer.param_groups)!=1 or self.optimizer.param_groups[0]['lr']!=READOUT_LR
                or any(p.grad is not None for p in self.model.parameters() if not p.requires_grad)):
            raise ValueError('Only fresh fixed-LR readout gradients/Adam are allowed')
        row.update(CE_loss=row['loss'],parameter_penalty=0.,parameter_coefficient=0.,parameter_penalty_teacher_tokens=0,
            native_optimizer_updates=0,readout_LR=READOUT_LR)
        return row
