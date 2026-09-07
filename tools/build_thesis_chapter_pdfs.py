#!/usr/bin/env python3
"""Build Scholar-friendly chapter PDFs from the official TU Delft thesis PDF."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


THESIS_TITLE = (
    "On the Methods for Explaining Polarization of Private and Unobservable "
    "Opinions: An Opinion-Behavior Co-Evolutionary Approach"
)
THESIS_DOI = "https://doi.org/10.4233/uuid:b4b02f3b-b622-4226-8f8c-be26e2c52428"


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    authors: tuple[str, ...]
    abstract: str
    thesis_pages: str
    first_pdf_index: int
    last_pdf_index: int
    slug: str
    output_name: str
    keywords: str


CHAPTERS = (
    Chapter(
        number=5,
        title=(
            "Modeling Opinion-Behavior Co-evolution for Explaining Opinion "
            "Polarization: A Framework"
        ),
        authors=("Tanzhe Tang", "Amineh Ghorbani", "Caspar G. Chorus"),
        abstract=(
            "The dynamics of opinions and behaviors are almost inseparable. Therefore, "
            "modeling opinion-behavior co-evolution is expected to be a more realistic "
            "approach to explaining opinion polarization than modeling opinion dynamics "
            "alone. Regardless of the co-evolution models that have already been proposed "
            "in various disciplines, this novel approach is still largely uncoordinated, "
            "and a unifying framework is in urgent need to organize existing efforts and "
            "facilitate future studies. In this paper, such a framework, called MOBEP "
            "(Modeling Opinion-Behavior Co-evolution for Explaining Opinion Polarization), "
            "is developed based on the central notion that behaviors serve as the "
            "messenger of opinions, highlighting the inference process that translates "
            "observed behaviors into inferred opinions. For validation purposes, the "
            "framework is applied to a selection of representative models. Finally, a "
            "case study about mask wearing during the COVID-19 pandemic is presented as "
            "a vivid demonstration of how the framework works."
        ),
        thesis_pages="111-154",
        first_pdf_index=121,
        last_pdf_index=164,
        slug="mobep-thesis-chapter",
        output_name="mobep-thesis-chapter.pdf",
        keywords=(
            "opinion-behavior co-evolution; opinion polarization; agent-based "
            "modeling framework; MOBEP"
        ),
    ),
    Chapter(
        number=6,
        title="Conclusions and Reflections",
        authors=("Tanzhe Tang",),
        abstract=(
            "This chapter concludes the efforts made in the thesis to achieve its "
            "research goals, with a special focus on the relations between the proposed "
            "methods. It identifies promising directions for future work, discusses the "
            "societal relevance of the thesis, and reflects on the field of opinion "
            "dynamics and polarization."
        ),
        thesis_pages="155-176",
        first_pdf_index=165,
        last_pdf_index=186,
        slug="conclusions-reflections-thesis-chapter",
        output_name="conclusions-reflections-thesis-chapter.pdf",
        keywords=(
            "opinion polarization; opinion dynamics; agent-based modeling; "
            "research methods; future research"
        ),
    ),
)


def draw_paragraph(
    pdf: canvas.Canvas,
    text: str,
    style: ParagraphStyle,
    x: float,
    y_top: float,
    width: float,
) -> float:
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, A4[1])
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def cover_page(chapter: Chapter) -> PdfReader:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4, pageCompression=1)
    width, height = A4
    left = 25 * mm
    content_width = width - (2 * left)
    y = height - 28 * mm

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ScholarTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=30,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#172B4D"),
        spaceAfter=0,
    )
    author_style = ParagraphStyle(
        "ScholarAuthors",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=18,
        leading=23,
        textColor=colors.HexColor("#243B53"),
    )
    label_style = ParagraphStyle(
        "Label",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#52606D"),
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#102A43"),
    )
    citation_style = ParagraphStyle(
        "Citation",
        parent=body_style,
        fontSize=9.5,
        leading=13.5,
        leftIndent=5 * mm,
        rightIndent=5 * mm,
    )

    y = draw_paragraph(pdf, chapter.title, title_style, left, y, content_width)
    y -= 8 * mm
    y = draw_paragraph(
        pdf,
        ", ".join(chapter.authors),
        author_style,
        left,
        y,
        content_width,
    )
    y -= 6 * mm

    pdf.setStrokeColor(colors.HexColor("#CBD5E1"))
    pdf.setLineWidth(0.8)
    pdf.line(left, y, width - left, y)
    y -= 8 * mm

    y = draw_paragraph(pdf, "THESIS CHAPTER", label_style, left, y, content_width)
    y -= 2 * mm
    provenance = (
        f"Chapter {chapter.number} (pp. {chapter.thesis_pages}) of the doctoral "
        f"dissertation <i>{THESIS_TITLE}</i>, Delft University of Technology, 2022. "
        "This standalone file reproduces the final published chapter and adds only "
        "this bibliographic cover page."
    )
    y = draw_paragraph(pdf, provenance, body_style, left, y, content_width)
    y -= 7 * mm

    y = draw_paragraph(pdf, "ABSTRACT", label_style, left, y, content_width)
    y -= 2 * mm
    y = draw_paragraph(pdf, chapter.abstract, body_style, left, y, content_width)
    y -= 7 * mm

    y = draw_paragraph(pdf, "RECOMMENDED CITATION", label_style, left, y, content_width)
    y -= 2 * mm
    if chapter.number == 5:
        citation = (
            "Tang, T., Ghorbani, A., &amp; Chorus, C. G. (2022). Modeling "
            "opinion-behavior co-evolution for explaining opinion polarization: A "
            f"framework. In T. Tang, <i>{THESIS_TITLE}</i> (Chapter 5, pp. "
            f"{chapter.thesis_pages}). Delft University of Technology."
        )
    else:
        citation = (
            "Tang, T. (2022). Conclusions and reflections. In T. Tang, "
            f"<i>{THESIS_TITLE}</i> (Chapter 6, pp. {chapter.thesis_pages}). "
            "Delft University of Technology."
        )
    y = draw_paragraph(pdf, citation, citation_style, left, y, content_width)
    y -= 7 * mm

    y = draw_paragraph(pdf, "SOURCE", label_style, left, y, content_width)
    y -= 2 * mm
    source = (
        f'Final published dissertation: <link href="{THESIS_DOI}" '
        f'color="#0B63CE">{THESIS_DOI}</link><br/>License: CC BY'
    )
    draw_paragraph(pdf, source, body_style, left, y, content_width)

    pdf.setFillColor(colors.HexColor("#52606D"))
    pdf.setFont("Helvetica", 8.5)
    pdf.drawString(left, 15 * mm, "Standalone copy of a dissertation chapter.")
    pdf.drawRightString(width - left, 15 * mm, "Delft University of Technology | 2022")

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return PdfReader(buffer)


def build_chapter(source: PdfReader, chapter: Chapter, output_root: Path) -> Path:
    writer = PdfWriter()
    writer.add_page(cover_page(chapter).pages[0])

    for page_index in range(chapter.first_pdf_index, chapter.last_pdf_index + 1):
        writer.add_page(source.pages[page_index])

    writer.add_metadata(
        {
            "/Title": chapter.title,
            "/Author": "; ".join(chapter.authors),
            "/Subject": (
                f"Chapter {chapter.number} of the doctoral dissertation {THESIS_TITLE}"
            ),
            "/Keywords": chapter.keywords,
            "/Creator": "Tanzhe Tang",
        }
    )

    output_dir = output_root / chapter.slug
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / chapter.output_name
    with output_path.open("wb") as output_file:
        writer.write(output_file)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Official complete thesis PDF")
    parser.add_argument("output_root", type=Path, help="Root directory for chapter files")
    args = parser.parse_args()

    args.output_root.mkdir(parents=True, exist_ok=True)
    source = PdfReader(args.source)
    if len(source.pages) != 198:
        raise ValueError(
            f"Expected the 198-page official thesis, found {len(source.pages)} pages"
        )

    for chapter in CHAPTERS:
        output_path = build_chapter(source, chapter, args.output_root)
        print(output_path)


if __name__ == "__main__":
    main()
