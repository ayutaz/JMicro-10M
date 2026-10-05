import sys
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/"scripts"))
from probe_textbook_supply import row_groups


def test_uniform_row_mapping_keeps_unequal_group_probabilities_and_every_edge():
    groups=row_groups([2,5,1],list(range(8)))
    assert groups=={0:[(0,0),(1,1)],1:[(2,0),(3,1),(4,2),(5,3),(6,4)],2:[(7,0)]}
    assert sum(len(g) for g in groups.values())==8
