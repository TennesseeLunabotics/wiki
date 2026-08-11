#!/usr/bin/env python3
"""Convert the repository's GitBook-flavored Markdown into MkDocs input.

Run this from the root of TennesseeLunabotics/wiki. It leaves the original
GitBook files untouched and regenerates ./docs for MkDocs.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
ASSET_SRC = ROOT / ".gitbook" / "assets"

TOP_LEVEL = ["README.md", "mission-statement.md"]
CONTENT_DIRS = ["systems-engineering", "programming"]


def transform(text: str) -> str:
    # GitBook content-ref wrappers add no semantic content beyond the Markdown
    # link nested inside them, so remove only the wrapper lines.
    text = re.sub(r"^\{%\s*content-ref\b.*?%\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\{%\s*endcontent-ref\s*%\}\s*$", "", text, flags=re.MULTILINE)

    # Preserve hint contents while removing GitBook-only delimiters. Material
    # will still render the inner Markdown cleanly.
    text = re.sub(r"^\{%\s*hint\b.*?%\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\{%\s*endhint\s*%\}\s*$", "", text, flags=re.MULTILINE)

    # GitBook asset directory is hidden. Copy it to docs/assets and rewrite
    # references without changing their relative-depth prefixes.
    text = text.replace(".gitbook/assets", "assets")

    # Subdirectory README files are emitted as index.md. Rewrite Markdown-link
    # destinations so links to those GitBook section landing pages keep working.
    text = re.sub(
        r"(?<=\()([^\n)]*?)(?:README\.md)(?=([#?][^)]*)?\))",
        lambda m: m.group(1) + "index.md",
        text,
        flags=re.IGNORECASE,
    )

    # GitBook exports sometimes include explicit nonbreaking-space entities.
    text = text.replace("&#x20;", "")

    # Collapse excessive blank lines introduced by removing template tags.
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def copy_markdown(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(transform(src.read_text(encoding="utf-8")), encoding="utf-8")


def main() -> None:
    if not (ROOT / "SUMMARY.md").exists():
        raise SystemExit(
            "Run prepare_docs.py from the TennesseeLunabotics/wiki repository root. "
            "SUMMARY.md was not found."
        )

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    for name in TOP_LEVEL:
        src = ROOT / name
        if not src.exists():
            continue
        dst_name = "index.md" if name == "README.md" else name
        copy_markdown(src, DOCS / dst_name)

    for dirname in CONTENT_DIRS:
        src_root = ROOT / dirname
        if not src_root.exists():
            continue
        for src in src_root.rglob("*.md"):
            rel = src.relative_to(ROOT)
            # README.md pages in subdirectories become index.md so their URLs
            # are /client/ and /server/, matching normal MkDocs conventions.
            if rel.name == "README.md":
                rel = rel.with_name("index.md")
            copy_markdown(src, DOCS / rel)

    if ASSET_SRC.exists():
        shutil.copytree(ASSET_SRC, DOCS / "assets", dirs_exist_ok=True)

    print(f"Prepared MkDocs sources in {DOCS}")


if __name__ == "__main__":
    main()
