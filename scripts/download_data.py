#!/usr/bin/env python
"""
Downloads the LOTR text files tarball.
If the URL is unavailable, manually place text files under data/raw/text_files/.
"""
import argparse
import tarfile
from pathlib import Path
import sys
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data/raw")
    parser.add_argument(
        "--url", 
        type=str,
        default="https://piazza.com/redirect/s3?bucket=uploads&prefix=attach%2Fjlifkda6h0x5bk%2Fhzosotq4zil49m%2Fjn13x09arfeb%2Ftext_files.tar.gz"
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tar_path = out_dir / "text_files.tar.gz"

    try:
        print(f"Downloading to {tar_path} ...")
        urllib.request.urlretrieve(args.url, tar_path)
        print("Extracting ...")
        with tarfile.open(tar_path, "r:gz") as tf:
            tf.extractall(out_dir)
        print("Done.")
    except Exception as e:
        print(f"Warning: download failed: {e}", file=sys.stderr)
        print("Create data manually under data/raw/text_files/*.txt", file=sys.stderr)

if __name__ == "__main__":
    main()
