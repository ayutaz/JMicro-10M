"""Model-blinded response packets and agreement, without fabricated human scores."""
import hashlib
import json
import random

from jmicro.chat_review import RUBRIC


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def make_packet(arms, seed):
    """Each arm has its evaluation SHA and all validated 219 review items.

    The private mapping is never put into the reviewer-facing packet. The seed
    is private too, so opaque IDs do not expose the checkpoint or route.
    """
    assert len(arms) >= 2 and len({a["evaluation_sha256"] for a in arms.values()}) == len(arms)
    keys = next(iter(arms.values()))["items"].keys()
    assert all(set(a["items"]) == set(keys) and len(a["items"]) == 219 for a in arms.values())
    jobs = [(name, key) for name, arm in arms.items() for key in arm["items"]]
    random.Random(seed).shuffle(jobs)
    public, private = [], []
    for number, (name, key) in enumerate(jobs, 1):
        item = arms[name]["items"][key]
        sample_id = f"review-{number:05d}"
        row = dict(sample_id=sample_id, messages=item["messages"], checks=item["checks"], response=item["response"]["text"])
        public.append(row)
        private.append(dict(sample_id=sample_id, arm=name, key=key, entry_sha256=digest(row)))
    packet = dict(schema="chat-blind-content-v1", rubric=RUBRIC, samples=public,
                  instructions="Score the response using the actual supplied conversation. Score grammar, relevance and context separately, without guessing the model. Empty or broken responses remain visible.")
    mapping = dict(schema="chat-blind-private-map-v1", private_seed=seed, samples=private,
                   arms={name: dict(evaluation_sha256=arm["evaluation_sha256"], checkpoint_sha256=arm["checkpoint_sha256"])
                         for name, arm in arms.items()})
    return packet, mapping


def notes_template(packet, packet_sha256):
    return dict(packet_sha256=packet_sha256,
        reviewer=dict(identity=None, kind="human", independent_human=None, blind=True),
        judgments=[dict(sample_id=r["sample_id"], grammar=None, relevance=None, context=None, rationale="") for r in packet["samples"]],
        instructions="A real human reviewer must supply their identity and independence declaration. Do not fill this as Codex or represent fixtures as human submissions.")


def restore_judgments(packet, packet_sha256, mapping, annotations):
    """Verify packet integrity and unwrap one actual human-declared submission.

    Integrity and blinding can be verified locally. Human identity is a
    declaration, not something token IDs or agreement statistics authenticate.
    """
    assert packet["schema"] == "chat-blind-content-v1" and packet["rubric"] == RUBRIC
    assert mapping["schema"] == "chat-blind-private-map-v1"
    assert mapping["packet_sha256"] == annotations["packet_sha256"] == packet_sha256
    public = {r["sample_id"]: r for r in packet["samples"]}
    links = {r["sample_id"]: r for r in mapping["samples"]}
    assert len(public) == len(packet["samples"]) == len(links) == len(mapping["samples"])
    assert len(public) == 219*len(mapping["arms"]) and set(public) == set(links)
    assert all(set(r) == {"sample_id", "messages", "checks", "response"} and digest(r) == links[k]["entry_sha256"] for k, r in public.items())
    reviewer = annotations["reviewer"]
    assert reviewer["kind"] == "human", "Codex/AI scores are not human submissions"
    assert isinstance(reviewer["identity"], str) and reviewer["identity"].strip()
    assert reviewer["independent_human"] is True and reviewer["blind"] is True
    rows = annotations["judgments"]
    scores = {r["sample_id"]: r for r in rows}
    assert len(rows) == len(scores) == len(public) and set(scores) == set(public), "Every blinded response needs a judgment"
    assert all(all(type(r[k]) is int and r[k] in (0, 1, 2) for k in ("grammar", "relevance", "context"))
               and isinstance(r["rationale"], str) and len(r["rationale"].strip()) >= 12 for r in rows)
    restored = {}
    for name, arm in mapping["arms"].items():
        matched = [(link, scores[k]) for k, link in links.items() if link["arm"] == name]
        assert len(matched) == 219 and len({link["key"] for link, _ in matched}) == 219
        restored[name] = dict(evaluation_sha256=arm["evaluation_sha256"], rubric=RUBRIC,
            reviewer=dict(kind="human_blind", identity=reviewer["identity"], independent_human=True, blind=True),
            judgments=[dict(key=link["key"], **{k: score[k] for k in ("grammar", "relevance", "context", "rationale")}) for link, score in matched],
            blind_packet_sha256=packet_sha256, human_identity_source="reviewer self-declaration; no external identity authentication")
    return restored


def agreement(left, right):
    """Exact agreement and unweighted Cohen kappa on the matched ordinal scores."""
    assert left["packet_sha256"] == right["packet_sha256"]
    identities = [n["reviewer"]["identity"] for n in (left, right)]
    assert all(isinstance(i, str) and i.strip() for i in identities)
    assert identities[0].strip().casefold() != identities[1].strip().casefold(), "Two distinct reviewers required"
    a = {r["sample_id"]: r for r in left["judgments"]}
    b = {r["sample_id"]: r for r in right["judgments"]}
    assert len(a) == len(left["judgments"]) == len(b) == len(right["judgments"]) and set(a) == set(b) and a
    result = {}
    for dimension in ("grammar", "relevance", "context"):
        matrix = [[0]*3 for _ in range(3)]
        for key in a:
            x, y = a[key][dimension], b[key][dimension]
            assert type(x) is type(y) is int and x in (0, 1, 2) and y in (0, 1, 2)
            matrix[x][y] += 1
        count = len(a)
        exact = sum(matrix[i][i] for i in range(3))/count
        expected = sum(sum(matrix[i])*sum(matrix[j][i] for j in range(3)) for i in range(3))/(count*count)
        result[dimension] = dict(responses=count, confusion_matrix=matrix, exact_agreement=exact,
            cohen_kappa=None if expected == 1. else (exact-expected)/(1.-expected),
            degenerate_expected_agreement=expected == 1.)
    return dict(dimensions=result, unit="response judgments; correlated turns/conditions, not independent dialogue families",
        statistical_note="Agreement is descriptive, not correctness, identity authentication, confidence intervals, or model quality certification")
