"""Read a pinned public Parquet footer; do not read any document bodies."""
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import pyarrow.parquet as pq
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json
from remote_parquet_ranges import RangeBudget, RangeFile, observed_size

OUT = ROOT / 'reports/phase6/base_hq_footer_inspection.json'


def main():
    if OUT.exists():
        raise ValueError('Preserve completed original footer inspection')
    start = time.monotonic()
    source = ROOT / 'reports/phase6/base_hq_source_feasibility.json'
    binding = json.loads(source.read_text())
    size = observed_size(binding['Content_Range'])
    url = f"https://huggingface.co/datasets/{binding['repository']}/resolve/{binding['revision']}/{binding['first_file']}"
    budget = RangeBudget(4 * 1024 * 1024, 30)
    try:
        with RangeFile(url, size, budget) as stream:
            parquet = pq.ParquetFile(stream, pre_buffer=False)
            metadata = parquet.metadata
            groups = []
            for index in range(metadata.num_row_groups):
                group = metadata.row_group(index)
                groups.append(dict(index=index, rows=group.num_rows, columns=[dict(
                    path=group.column(k).path_in_schema, compressed_bytes=group.column(k).total_compressed_size)
                    for k in range(group.num_columns)]))
            report = dict(status='pinned_footer_only_observed', created_at=now(),
                source_sha256=sha256(source), repository=binding['repository'], revision=binding['revision'],
                file=binding['first_file'], file_bytes=size, rows=metadata.num_rows,
                schema=str(parquet.schema_arrow), row_groups=groups,
                remote_bytes=budget.bytes, HTTP_range_requests=budget.requests,
                wall_seconds=time.monotonic() - start, corpus_records_downloaded=0,
                prepared_training_tokens=0, scientific_teacher_tokens=0, GPU_seconds=0,
                Base_complete=False, Chat_started=False, quantization_started=False,
                limits=dict(remote_bytes=4 * 1024 * 1024, wall_seconds=30),
                reader_sha256=sha256(ROOT / 'scripts/remote_parquet_ranges.py'),
                source_records_and_embeddings_not_read=True,
                next_action='Freeze a bounded selected-column TRAIN-source sample using actual group sizes; preserve old-family exact/URL exclusions without reading protected test bodies. Sample suitability is not corpus acceptance.')
    except Exception as error:
        # Do not serialize URLs or signed redirect exceptions.
        report = dict(status='footer_inspection_failed_preserved', created_at=now(),
            error_type=type(error).__name__, remote_bytes=budget.bytes, HTTP_range_requests=budget.requests,
            wall_seconds=time.monotonic()-start, prepared_training_tokens=0, GPU_seconds=0,
            next_action='Inspect the bounded failure; no identical retry or full-file fallback.')
        atomic_json(OUT, report)
        raise RuntimeError('Bounded footer inspection failed; original report saved') from None
    atomic_json(OUT, report)
    print({k:report[k] for k in ('status', 'rows', 'remote_bytes', 'HTTP_range_requests', 'wall_seconds')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
