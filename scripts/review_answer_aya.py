"""Bind the 120 explicitly authored Aya QA decisions to original selected fields."""
from collections import Counter
from answer_learning_common import RUN, DATA, save, ref, bound, read_json, now


def main():
    target=RUN/'aya_QA_review.json'; assert not target.exists()
    inventory=read_json(RUN/'aya_inventory.json'); rows=read_json(bound(inventory['sample']))
    notes=read_json(RUN/'aya_QA_authored.json'); assert len(rows)==len(notes)==120
    result=[]; counts=Counter()
    for row,(uid,accepted,reason) in zip(rows,notes,strict=True):
        assert uid==row['id'] and type(accepted) is bool and len(reason)>=12
        result.append(dict(id=uid,doc_id=row['doc_id'],accepted_for_next_recipe=accepted,rationale=reason,
            original_selected_fields_sha256=row['original_selected_fields_sha256']))
        counts['reviewed']+=1; counts['accepted']+=accepted
        counts[row['annotation_type']+':accepted']+=accepted
    save(target,dict(status='all120_individual_QA_complete',created_at=now(),inventory=ref(RUN/'aya_inventory.json'),
        sample=inventory['sample'],authored=ref(RUN/'aya_QA_authored.json'),judgments=result,counts=dict(counts),
        reviewer='Codex nonblind; full selected inputs and original targets displayed; no independent human',
        caveats=['Purposive annotation-type/length sample, not population accuracy',
            'Niche factual answers declined without independent verification are not proved wrong',
            'Historical relative-time questions are not valid timeless assistant teaching examples',
            'Accepted provided-text summaries do not certify source factual truth'],
        upstream_TEST_used=False,new_training_updates=0))
    print(dict(counts))


if __name__=='__main__':main()
