#!/usr/bin/env python3
"""Generate Horizon Europe-structured DMP PDF (stdlib only, no pip deps)."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MD_PATH = REPO_ROOT / "DataManagementPlan" / "DMP_CNM_HE_v1.1.md"
PDF_PATH = REPO_ROOT / "DataManagementPlan" / "DMP_CNM_HE_v1.1.pdf"


def _escape_pdf(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class SimplePDF:
    """Minimal PDF writer for text documents."""

    def __init__(self) -> None:
        self.pages: list[list[str]] = []
        self._page: list[str] = []
        self.y = 800
        self.page_height = 842
        self.margin = 50
        self.line_height = 14

    def add_page(self) -> None:
        if self._page:
            self.pages.append(self._page)
        self._page = []
        self.y = 800

    def _check_page(self, needed: int = 20) -> None:
        if self.y - needed < 60:
            self.add_page()

    def text(self, content: str, size: int = 11, bold: bool = False) -> None:
        font = "/F2" if bold else "/F1"
        for paragraph in content.split("\n"):
            paragraph = paragraph.strip()
            if not paragraph:
                self.y -= self.line_height // 2
                continue
            wrapped = textwrap.wrap(paragraph, width=92)
            for line in wrapped:
                self._check_page()
                self._page.append(
                    f"BT {font} {size} Tf 1 0 0 1 {self.margin} {self.y} Tm ({_escape_pdf(line)}) Tj ET"
                )
                self.y -= self.line_height

    def title(self, content: str, size: int = 14) -> None:
        self.y -= 8
        self.text(content, size=size, bold=True)
        self.y -= 4

    def table(self, headers: list[str], rows: list[list[str]]) -> None:
        if not rows:
            return
        col_w = 490 // len(headers)
        self._check_page(30)
        x0 = self.margin
        row_h = 16
        # header
        for i, h in enumerate(headers):
            x = x0 + i * col_w
            self._page.append(
                f"BT /F2 8 Tf 1 0 0 1 {x} {self.y} Tm ({_escape_pdf(h[:28])}) Tj ET"
            )
        self.y -= row_h
        for row in rows:
            self._check_page()
            for i, cell in enumerate(row):
                x = x0 + i * col_w
                self._page.append(
                    f"BT /F1 8 Tf 1 0 0 1 {x} {self.y} Tm ({_escape_pdf(str(cell)[:32])}) Tj ET"
                )
            self.y -= row_h
        self.y -= 6

    def build(self, path: Path) -> None:
        if self._page:
            self.pages.append(self._page)
        if not self.pages:
            self.add_page()

        objects: list[bytes] = []
        kids: list[str] = []

        def add_obj(data: str | bytes) -> str:
            if isinstance(data, str):
                data = data.encode("latin-1", errors="replace")
            objects.append(data)
            return str(len(objects))

        font_regular = add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
        font_bold = add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

        for stream_lines in self.pages:
            stream = "\n".join(stream_lines)
            content_id = add_obj(f"<< /Length {len(stream)} >>\nstream\n{stream}\nendstream")
            page_id = add_obj(
                f"<< /Type /Page /Parent {{parent}} 0 R /MediaBox [0 0 595 842] "
                f"/Contents {content_id} 0 R /Resources << /Font << /F1 {font_regular} 0 R /F2 {font_bold} 0 R >> >> >>"
            )
            kids.append(page_id)

        kids_str = " ".join(f"{k} 0 R" for k in kids)
        pages_id = add_obj(f"<< /Type /Pages /Kids [{kids_str}] /Count {len(kids)} >>")

        for i, obj in enumerate(objects):
            if b"/Parent {parent}" in obj:
                objects[i] = obj.replace(b"{parent}", f"{pages_id} ".encode())

        catalog_id = add_obj(f"<< /Type /Catalog /Pages {pages_id} 0 R >>")

        out = bytearray(b"%PDF-1.4\n")
        offsets = [0]
        for i, obj in enumerate(objects, start=1):
            offsets.append(len(out))
            out.extend(f"{i} 0 obj\n".encode())
            out.extend(obj)
            out.extend(b"\nendobj\n")

        xref_pos = len(out)
        out.extend(f"xref\n0 {len(objects)+1}\n".encode())
        out.extend(b"0000000000 65535 f \n")
        for off in offsets[1:]:
            out.extend(f"{off:010d} 00000 n \n".encode())
        out.extend(
            f"trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\n"
            f"startxref\n{xref_pos}\n%%EOF\n".encode()
        )
        path.write_bytes(out)


def parse_tables(block: str) -> tuple[str, list[tuple[list[str], list[list[str]]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    lines = block.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "|" in line and i + 1 < len(lines) and re.match(r"^\|?[\s\-:|]+\|", lines[i + 1]):
            headers = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i]:
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            tables.append((headers, rows))
            continue
        out.append(line)
        i += 1
    return "\n".join(out), tables


def build_pdf() -> Path:
    raw = MD_PATH.read_text(encoding="utf-8").replace("**", "").replace("`", "")
    pdf = SimplePDF()
    pdf.add_page()

    pdf.title("Data Management Plan", size=18)
    pdf.text("CNM — Semiconductor Device Characterization Data (180 nm CMOS)")
    pdf.text("Template: Horizon Europe DMP v1.1 (01.04.2022)")
    pdf.text("Version 1.1 | Date: 10/06/2025 | Public | Uzziel Perez")
    pdf.text("uzzielperez25@gmail.com | github.com/uzzielperez/CNM")
    pdf.add_page()

    for chunk in re.split(r"\n(?=## )", raw)[1:]:
        m = re.match(r"^## (.+)$", chunk, re.MULTILINE)
        if not m:
            continue
        section = m.group(1).strip()
        body = chunk.split("\n", 1)[1] if "\n" in chunk else ""
        pdf.title(section)

        if section.lower() == "history of changes":
            _, tables = parse_tables(body)
            for headers, rows in tables:
                pdf.table(headers, rows)
            continue

        for part in re.split(r"\n(?=### )", body):
            part = part.strip()
            if not part:
                continue
            sm = re.match(r"^### (.+)$", part, re.MULTILINE)
            if sm:
                pdf.title(sm.group(1), size=12)
                part = part.split("\n", 1)[1] if "\n" in part else ""
            part, tables = parse_tables(part)
            for headers, rows in tables:
                pdf.table(headers, rows)
            lines = [ln.strip() for ln in part.splitlines() if ln.strip() and not ln.strip().startswith("---")]
            bullets = [ln[2:] for ln in lines if ln.startswith("- ")]
            prose = [ln for ln in lines if not ln.startswith("- ") and not ln.startswith("|")]
            if prose:
                pdf.text("\n".join(prose))
            for b in bullets:
                pdf.text(f"• {b}")

    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf.build(PDF_PATH)
    return PDF_PATH


if __name__ == "__main__":
    out = build_pdf()
    print(f"Wrote {out}")
