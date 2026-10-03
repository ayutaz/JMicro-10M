"""Parallel verification of the same frozen LSH candidates, with global merging.

This is an optional execution path. Ingestion, quality filters, signature scheme,
Jaccard threshold and split rules are unchanged. Never discard a candidate because
of a sample, estimated MinHash similarity or a group-size cap.
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import lru_cache
import multiprocessing
from pathlib import Path
import sqlite3
import time

import numpy as np

from jmicro.corpus_state import read_json, write_json
from jmicro.data import normalized, overlap, shingles
from jmicro.experiment import sha256
from jmicro.large_corpus import Groups, band_order


def verify_band(task):
    directory, ids_path, n, band, destination = task
    directory, destination = Path(directory), Path(destination)
    ids = np.load(ids_path, mmap_mode="r")
    sketches = np.memmap(directory/"signatures.u32.bin", mode="r", dtype="<u4", shape=(n,128))
    db = sqlite3.connect(f'file:{directory/"records.sqlite"}?mode=ro', uri=True)
    db.execute("PRAGMA cache_size=-16384")
    started = time.perf_counter()
    ordered, bounds = band_order(sketches, ids, band)
    sort_seconds = time.perf_counter()-started
    local = Groups(n)
    links = []
    candidates = checked = 0

    @lru_cache(maxsize=2048)
    def features(i):
        return shingles(normalized(db.execute("SELECT text FROM records WHERE id=?", (i,)).fetchone()[0]),5)

    # Only singleton groups are skipped, without altering any candidate pairs.
    for index in np.flatnonzero(np.diff(bounds)>1):
        members = ordered[bounds[index]:bounds[index+1]]
        for pos,a in enumerate(members):
            for b in members[:pos]:
                candidates += 1
                if local.find(a)==local.find(b):
                    continue
                checked += 1
                if overlap(features(int(a)),features(int(b)))>=.85:
                    local.union(a,b)
                    links.append((int(a),int(b)))
    db.close()
    destination.mkdir(parents=True,exist_ok=True)
    path = destination/f"band-{band:02d}.edges.npy"
    np.save(path,np.asarray(links,dtype=np.uint32).reshape(-1,2))
    result = {"band":band,"candidate_pairs":candidates,"checked_pairs":checked,
              "verified_links":len(links),"sort_seconds":sort_seconds,
              "elapsed_seconds":time.perf_counter()-started,"edges_sha256":sha256(path)}
    write_json(destination/f"band-{band:02d}.json",result)
    return result


def parallel_components(directory, destination, n, workers=8, bands=32):
    """Save band edges/checkpoints; return deterministic minimum representatives."""
    directory,destination=Path(directory),Path(destination)
    destination.mkdir(parents=True,exist_ok=True)
    ids_path=destination/"eligible_ids.npy"
    db=sqlite3.connect(f'file:{directory/"records.sqlite"}?mode=ro',uri=True)
    if not ids_path.exists():
        ids=np.fromiter((r[0] for r in db.execute(
            "SELECT id FROM records WHERE sketch=1 AND id<? ORDER BY id",(n,))),dtype=np.uint32)
        np.save(ids_path,ids)
        write_json(destination/"scope.json",{"records":n,"eligible_records":len(ids),
                                             "ids_sha256":sha256(ids_path),"bands":bands})
    scope=read_json(destination/"scope.json")
    if scope["records"]!=n or scope["bands"]!=bands or sha256(ids_path)!=scope["ids_sha256"]:
        raise ValueError("Parallel execution scope changed")
    tasks=[]
    reports={}
    for band in range(bands):
        report_path=destination/f"band-{band:02d}.json"
        if report_path.exists():
            report=read_json(report_path)
            if sha256(destination/f"band-{band:02d}.edges.npy")!=report["edges_sha256"]:
                raise ValueError("Verified band edge checkpoint changed")
            reports[band]=report
        else:
            tasks.append((str(directory),str(ids_path),n,band,str(destination)))
    started=time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers,mp_context=multiprocessing.get_context("spawn")) as executor:
        pending=[executor.submit(verify_band,task) for task in tasks]
        for future in as_completed(pending):
            report=future.result()
            reports[report["band"]]=report
            write_json(destination/"progress.json",{"completed_bands":len(reports),"bands":bands,
                                                      "elapsed_seconds":time.perf_counter()-started})
    groups,duplicates=Groups(n),Groups(n)
    for a,b,duplicate in db.execute("SELECT a,b,duplicate FROM edges WHERE a<? AND b<?",(n,n)):
        groups.union(a,b)
        if duplicate:
            duplicates.union(a,b)
    db.close()
    for band in range(bands):
        edges=np.load(destination/f"band-{band:02d}.edges.npy",mmap_mode="r")
        for a,b in edges:
            groups.union(a,b)
            duplicates.union(a,b)
    for i in range(n):
        groups.parent[i]=groups.find(i)
        duplicates.parent[i]=duplicates.find(i)
    np.save(destination/"groups.npy",groups.parent)
    np.save(destination/"duplicates.npy",duplicates.parent)
    result={"status":"verified_components_built","records":n,"workers":workers,"bands":bands,
            "elapsed_seconds":time.perf_counter()-started,
            "candidate_pairs":sum(r["candidate_pairs"] for r in reports.values()),
            "verified_links":sum(r["verified_links"] for r in reports.values()),
            "groups_sha256":sha256(destination/"groups.npy"),
            "duplicates_sha256":sha256(destination/"duplicates.npy")}
    write_json(destination/"result.json",result)
    return result
