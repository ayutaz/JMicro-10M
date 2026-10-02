"""Fetch the pinned public llama.cpp source and build CPU tools + ID bridge."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REVISION = "46ca246de9bb1c35269722a6240d37d9dfd79cad"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="Download the fixed revision if absent")
    args = parser.parse_args()
    runtime = ROOT / "artifacts/runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    archive = runtime / "llama-source.tar.gz"
    source = runtime / "llama.cpp"
    build = runtime / "build"
    url = f"https://api.github.com/repos/ggml-org/llama.cpp/tarball/{REVISION}"
    if not archive.exists():
        if not args.fetch:
            raise SystemExit("Source absent; rerun with --fetch")
        with urllib.request.urlopen(url) as response, archive.open("wb") as output:
            import shutil
            shutil.copyfileobj(response, output)
    if not source.exists():
        source.mkdir()
        with tarfile.open(archive) as tar:
            members = tar.getmembers()
            # GitHub adds a revision-specific directory. Strip just that prefix.
            for member in members:
                parts = Path(member.name).parts[1:]
                if not parts:
                    continue
                member.name = str(Path(*parts))
                tar.extract(member, source, filter="data")
    flags = ["-DCMAKE_BUILD_TYPE=Release", "-DGGML_METAL=OFF", "-DGGML_BLAS=OFF",
             "-DGGML_ACCELERATE=OFF", "-DGGML_CCACHE=OFF", "-DCMAKE_C_COMPILER_LAUNCHER=",
             "-DCMAKE_CXX_COMPILER_LAUNCHER=", "-DLLAMA_BUILD_TESTS=OFF", "-DLLAMA_BUILD_EXAMPLES=OFF",
             "-DLLAMA_BUILD_SERVER=OFF", "-DLLAMA_BUILD_MTMD=OFF", "-DLLAMA_BUILD_TOOLS=ON"]
    commands = [["cmake", "-S", str(source), "-B", str(build), *flags],
                ["cmake", "--build", str(build), "--target", "llama-quantize", "llama-completion", "-j", "4"],
                ["cmake", "-S", str(ROOT / "scripts/native"), "-B", str(runtime / "build-bridge"),
                 "-DCMAKE_BUILD_TYPE=Release", "-DCMAKE_CXX_COMPILER_LAUNCHER=",
                 f"-DLLAMA_SOURCE_DIR={source}", f"-DLLAMA_BUILD_DIR={build}",
                 f"-DCMAKE_RUNTIME_OUTPUT_DIRECTORY={runtime}"],
                ["cmake", "--build", str(runtime / "build-bridge"), "-j", "2"]]
    with (runtime / "build.log").open("w") as log:
        for command in commands:
            subprocess.run(command, check=True, stdout=log, stderr=log)
    receipt = {"revision": REVISION, "source_url": url, "archive_sha256": digest(archive),
               "commands": commands, "bridge_source_sha256": digest(ROOT / "scripts/llama_bridge.cpp"),
               "bridge_binary_sha256": digest(runtime / "llama-bridge"),
               "quantizer_binary_sha256": digest(build / "bin/llama-quantize"),
               "completion_binary_sha256": digest(build / "bin/llama-completion"),
               "note": "Archive checkout; embedded git build version can inherit parent repo and is not revision evidence"}
    (runtime / "source_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "built", "revision": REVISION, "receipt": str(runtime / "source_receipt.json")}))


if __name__ == "__main__":
    main()
