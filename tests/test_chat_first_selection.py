"""A failed screen never becomes a selected candidate; ties favor earlier SFT."""
import sys
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from compare_chat_first_sft import select_checkpoint


def test_screen_repetition_and_fixed_order():
    rows=[dict(epoch=1,dev_screen_passed=True,joint=60,context=16,repetition=2),
        dict(epoch=2,dev_screen_passed=True,joint=60,context=16,repetition=2),
        dict(epoch=3,dev_screen_passed=False,joint=80,context=24,repetition=0)]
    selected,best=select_checkpoint(rows,2)
    assert selected['epoch']==1 and best['epoch']==3
    assert select_checkpoint(rows,1)[0] is None
    assert select_checkpoint([dict(r,dev_screen_passed=False) for r in rows],100)[0] is None
