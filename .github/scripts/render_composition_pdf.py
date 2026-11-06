"""Render a FHIR Composition to a PDF, following FHIR document presentation rules.

The PDF is the concatenation of:

- a banner generated from the subject Patient (name, date of birth, gender,
  address, phone, email),
- the Composition's own narrative (Composition.text),
- each section's title and narrative (Composition.section.title/text),

laid out on A4 with Helvetica, as used for the Alex story discharge summary.

The subject Patient is found by resourceType/id among the JSON files in the
Composition's directory. Optionally the rendered PDF also replaces the PDF
attachment data in a DocumentReference, so the standalone PDF and the
DocumentReference stay identical.

Requires reportlab (pip install reportlab). Output is deterministic: running
the script twice on the same input gives the same bytes.

Example:

    python .github/scripts/render_composition_pdf.py \\
        au-fhir-test-data-set/connected-care/alex-story/Composition-dischargesummary-thompson-alex-20251101.json \\
        "au-fhir-test-data-set/connected-care/alex-story/Discharge Summary - Alex Thompson - 2025-11-01.pdf" \\
        --docref au-fhir-test-data-set/connected-care/alex-story/DocumentReference-dischargesummary-thompson-alex-20251101.json
"""

import argparse
import base64
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate

XHTML = "{http://www.w3.org/1999/xhtml}"
INLINE_TAGS = {"b": "b", "strong": "b", "i": "i", "em": "i"}

TITLE = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=18, leading=22, spaceAfter=6)
HEADING = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=13, leading=18, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=4)


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_resource(directory, reference):
    """Return the resource in directory whose resourceType/id matches reference."""
    for path in sorted(Path(directory).glob("*.json")):
        try:
            resource = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if f"{resource.get('resourceType')}/{resource.get('id')}" == reference:
            return resource
    raise SystemExit(f"{reference} not found in {directory}")


def inline_markup(element):
    """Convert an XHTML element's content to ReportLab paragraph markup."""
    parts = [escape(element.text or "")]
    for child in element:
        tag = child.tag.replace(XHTML, "")
        if tag == "br":
            parts.append("<br/>")
        elif tag in INLINE_TAGS:
            parts.append(f"<{INLINE_TAGS[tag]}>{inline_markup(child)}</{INLINE_TAGS[tag]}>")
        else:
            parts.append(inline_markup(child))
        parts.append(escape(child.tail or ""))
    return "".join(parts)


def narrative_paragraphs(div):
    """Split a narrative div into paragraphs: one per <p>, or one for the whole div."""
    root = ET.fromstring(div)
    blocks = [child for child in root if child.tag.replace(XHTML, "") in ("p", "div")]
    if not blocks:
        return [Paragraph(inline_markup(root), BODY)]
    return [Paragraph(inline_markup(block), BODY) for block in blocks]


def patient_name(patient):
    names = patient.get("name", [])
    name = next((n for n in names if n.get("use") == "official"), names[0] if names else {})
    if "text" in name:
        return name["text"]
    return " ".join(name.get("given", []) + [name.get("family", "")]).strip()


def patient_banner(patient):
    fields = [("Name", patient_name(patient)), ("Date of Birth", patient.get("birthDate")), ("Gender", patient.get("gender"))]
    if patient.get("address"):
        address = patient["address"][0]
        parts = address.get("line", []) + [address.get(k) for k in ("city", "state", "postalCode")]
        fields.append(("Address", ", ".join(p for p in parts if p)))
    for system, label in (("phone", "Phone"), ("email", "Email")):
        telecom = next((t for t in patient.get("telecom", []) if t.get("system") == system), None)
        if telecom:
            fields.append((label, telecom["value"]))
    return [Paragraph(f"<b>{label}</b>: {escape(value)}", BODY) for label, value in fields if value]


def document_title(composition):
    coding = composition.get("type", {}).get("coding", [{}])[0]
    return composition.get("type", {}).get("text") or coding.get("display", "Document").title()


def render(composition_path, output_path):
    composition = load_json(composition_path)
    patient = find_resource(Path(composition_path).parent, composition["subject"]["reference"])
    title = document_title(composition)
    authors = [a.get("display") for a in composition.get("author", []) if a.get("display")]

    story = [
        Paragraph(escape(title), TITLE),
        HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#888888"), spaceBefore=2, spaceAfter=8),
        Paragraph("Patient", HEADING),
        *patient_banner(patient),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceBefore=6, spaceAfter=8),
    ]
    if composition.get("text", {}).get("div"):
        story += narrative_paragraphs(composition["text"]["div"])
    for section in composition.get("section", []):
        story.append(Paragraph(escape(section.get("title", "")), HEADING))
        if section.get("text", {}).get("div"):
            story += narrative_paragraphs(section["text"]["div"])

    rl_config.invariant = 1
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title=f"{title} - {patient_name(patient)}",
        author=", ".join(authors),
    )
    doc.build(story)


def update_document_reference(docref_path, pdf_path):
    """Replace the PDF attachment data in a DocumentReference, keeping its formatting."""
    path = Path(docref_path)
    text = path.read_text(encoding="utf-8")
    attachments = [c["attachment"] for c in json.loads(text)["content"] if c["attachment"].get("contentType") == "application/pdf"]
    if len(attachments) != 1 or "data" not in attachments[0]:
        raise SystemExit(f"{docref_path}: expected exactly one PDF attachment with data")
    old = attachments[0]["data"]
    new = base64.b64encode(Path(pdf_path).read_bytes()).decode("ascii")
    path.write_text(text.replace(old, new), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render a FHIR Composition to a PDF.")
    parser.add_argument("composition", help="Composition JSON file")
    parser.add_argument("output", help="PDF file to write")
    parser.add_argument("--docref", help="DocumentReference JSON whose PDF attachment data is replaced")
    args = parser.parse_args(argv)

    render(args.composition, args.output)
    print(f"Wrote {args.output}")
    if args.docref:
        update_document_reference(args.docref, args.output)
        print(f"Updated {args.docref}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
