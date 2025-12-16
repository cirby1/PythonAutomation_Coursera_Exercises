import os

from pathlib import Path

dest_dir = Path("/.test1/")
if not dest_dir.exists():
    dest_dir.mkdir()

src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

src_file.rename(dest_file)
