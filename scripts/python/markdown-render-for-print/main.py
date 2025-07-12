#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def render_markdown(md_path_str: str, output_format: str = "pdf"):
    md_path = Path(md_path_str).resolve()
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    output_ext = "pdf" if output_format == "pdf" else "html"
    output_path = md_path.with_suffix(f".{output_ext}")

    cmd = ["pandoc", str(md_path), "-o", str(output_path)]

    if output_format == "pdf":
        cmd += ["--pdf-engine=xelatex"]
    elif output_format == "html":
        cmd += ["--standalone", "--css=github.css"]  # optional styling

    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"{output_format.upper()} generated: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: markdown_render.py path/to/file.md [pdf|html]")
        sys.exit(1)

    render_markdown(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "pdf")
