"""Whole raw fixed64 content decision with the original predeclared gates."""
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_translated_story_source import RUN
from translated_story_source import TranslatedStoryTrainView


def main():
    if (RUN/'content-review.json').exists():raise ValueError('Preserve actual terminal content decision')
    job=read_json(RUN/'job.json');m=read_json(RUN/'manifest.json');pilot=read_json(RUN/'content-pilot.json')
    raw=read_json(RUN/'content-notes.json');notes=raw['notes'];rows={r['id']:r for r in pilot['rows']}
    if (job['status']!='complete_pending_fixed64_content' or alive(job) or job['manifest_sha256']!=sha256(RUN/'manifest.json')
            or m['pilot_sha256']!=sha256(RUN/'content-pilot.json') or raw['pilot_sha256']!=m['pilot_sha256']
            or not raw['all64_individually_read'] or len(notes)!=64 or len({n['id'] for n in notes})!=64
            or {n['id'] for n in notes}!=set(rows)):
        raise ValueError('Terminal source and every raw-bound fixed64 observation required')
    for note in notes:
        if (note['text_sha256']!=rows[note['id']]['text_sha256'] or type(note['content_quality']) is not int
                or note['content_quality'] not in (0,1,2) or type(note['weak_document']) is not bool
                or note['weak_document']!=(note['content_quality']!=2) or type(note['unresolved_grammar_issue']) is not bool
                or type(note['unresolved_grounding_issue']) is not bool or len(note['reason'])<12):
            raise ValueError('Exact whole content/rubric/individual rationale required')
    weak=sum(n['weak_document'] for n in notes);grammar=sum(n['unresolved_grammar_issue'] for n in notes)
    grounding=sum(n['unresolved_grounding_issue'] for n in notes);accepted=weak<=10 and grammar==grounding==0
    report=dict(status='all64_pinned_original_translation_content_review_complete',created_at=now(),all64_read=True,
        weak_documents=weak,maximum_weak_documents=10,unresolved_grammar_documents=grammar,unresolved_grounding_documents=grounding,
        training_pool_accepted=accepted,manifest_sha256=sha256(RUN/'manifest.json'),pilot_sha256=m['pilot_sha256'],
        notes_sha256=sha256(RUN/'content-notes.json'),notes=notes,reviewer='Codex nonblind',independent_human_blind=False,
        external_fact_certification=False,source_or_selection_modified=False,
        scientific_teacher_tokens=0,GPU_seconds=0,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Fixed64 new content calibration from original TRAIN translations; no independent human/global corpus quality guarantee or model training evidence.')
    atomic_json(RUN/'content-review.json',report)
    atomic_json(ROOT/'reports/phase6/translated_story_source_content_review.json',report)
    if accepted:TranslatedStoryTrainView(RUN,job['manifest_sha256'])
    print(dict(weak_documents=weak,unresolved_grammar_documents=grammar,unresolved_grounding_documents=grounding,source_accepted=accepted))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
