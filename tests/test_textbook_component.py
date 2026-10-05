import sys
from jmicro.experiment import ROOT, read_json
from jmicro.tokenizer import Tokenizer
sys.path.insert(0, str(ROOT/"scripts"))
import prepare_textbook_component as component


def test_native_worker_keeps_source_coordinates_ids_and_sibling_grade_split():
    path = ROOT/"artifacts/phase2/4096/tokenizer.model"
    component.worker_init(str(path))
    tok = Tokenizer(path)
    text = ("雨が降ると地面に水がしみ込みます。土の中には小さなすき間があり、水はそのすき間を通って下へ流れます。"
            "木の根は土の中の水を吸い上げます。葉から水が空気中へ出ることで、根から葉まで水が運ばれます。")
    rows = [(7, dict(source_id="article-A", url="https://example.invalid/A", rewrite=text,
                     prompt_type="elementary-school")),
            (19, dict(source_id="article-A", url="https://example.invalid/A", rewrite=text,
                      prompt_type="high-school"))]
    units, processed, native = component.worker(("train-00001.parquet", rows))
    assert processed == 2 and native == 2*len(tok.encode(text)) and units
    assert {u["source_row"] for u in units} == {7,19}
    assert len({u["source_family"] for u in units}) == len({u["split"] for u in units}) == 1
    for u in units:
        assert u["source"] == "textbook" and u["source_file"] == "train-00001.parquet"
        assert u["token_ids"] == [2,*tok.encode(u["text"]),3]
        assert u["text"] == text[u["source_char_start"]:u["source_char_end"]]


def test_previously_inspected_families_can_all_be_excluded_without_grade_leakage():
    document = read_json(ROOT/"reports/phase6/textbook_supply_sample32.json")
    excluded = {u["source_family"] for u in document["examples"]}
    assert len(document["examples"]) == len(excluded) == 32
    component.worker_init(str(ROOT/"artifacts/phase2/4096/tokenizer.model"))
    row = dict(source_id=document["examples"][0]["source_id"], url="https://example.invalid/source",
        prompt_type="high-school", rewrite=("雨が降ると地面に水がしみ込みます。土の中には小さなすき間があり、水はそのすき間を通って下へ流れます。"
            "木の根は土の中の水を吸い上げます。葉から水が空気中へ出ることで、根から葉まで水が運ばれます。"))
    units, _, _ = component.worker(("train-00002.parquet", [(3,row)]))
    assert units and all(u["source_family"] in excluded for u in units)
