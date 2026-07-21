"""Generate the Letter of Explanation (business tax filing) PDF for Vectra Core Systems LLC."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

OUTPUT = "Vectra_Core_Systems_Tax_Explanation_Letter.pdf"

styles = getSampleStyleSheet()
normal = ParagraphStyle(
    "body", parent=styles["Normal"], fontName="Times-Roman",
    fontSize=11.5, leading=16,
)
justified = ParagraphStyle("just", parent=normal, alignment=TA_JUSTIFY)
subject = ParagraphStyle("subj", parent=normal, fontName="Times-Bold")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=1 * inch, rightMargin=1 * inch,
    topMargin=1 * inch, bottomMargin=1 * inch,
)

story = []

story.append(Paragraph("July 13, 2026", normal))
story.append(Spacer(1, 18))

recipient = [
    "Dara Sailler",
    "Program Assistant",
    "Office of Equal Opportunity",
    "301 W. High St., Suite 870B",
    "Jefferson City, MO 65101",
    "Phone: 573-751-8130",
    "Email: dara.sailler@oa.mo.gov",
]
for line in recipient:
    story.append(Paragraph(line, normal))
story.append(Spacer(1, 18))

story.append(Paragraph(
    "Subject: Letter of Explanation — Business Tax Filing for "
    "Vectra Core Systems LLC (UEI V9N4N8M4K8A1)", subject))
story.append(Spacer(1, 18))

story.append(Paragraph("Dear Ms. Sailler,", normal))
story.append(Spacer(1, 12))

story.append(Paragraph(
    "Vectra Core Systems LLC is a newly formed single-member limited liability "
    "company and has not yet filed a company tax return. The business is 100% "
    "owned by Manse Soura and is currently operating using personal capital "
    "alongside a dedicated business bank account.", justified))
story.append(Spacer(1, 12))

story.append(Paragraph(
    "Supporting documentation, including the EIN confirmation and business bank "
    "account statements, is available upon request. Additionally, a signed and "
    "dated Operating Agreement and an organizational chart can be provided "
    "promptly.", justified))
story.append(Spacer(1, 12))

story.append(Paragraph(
    "Please advise if any further documentation or clarification is required. "
    "Thank you for your consideration.", justified))
story.append(Spacer(1, 24))

story.append(Paragraph("Sincerely,", normal))
story.append(Spacer(1, 30))

closing = [
    "Manse Soura",
    "Founder, Vectra Core Systems LLC",
    "contracts@vectracoresystems.com | +1 254-216-0899",
]
for line in closing:
    story.append(Paragraph(line, normal))

doc.build(story)
print("Wrote", OUTPUT)
