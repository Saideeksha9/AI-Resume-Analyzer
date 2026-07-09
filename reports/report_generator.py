from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_report(score, skills, missing, suggestions):

    filename = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["BodyText"]))

    story.append(Paragraph("<b>Skills Found:</b>", styles["Heading2"]))
    story.append(Paragraph(", ".join(skills), styles["BodyText"]))

    story.append(Paragraph("<b>Missing Skills:</b>", styles["Heading2"]))

    if missing:
        story.append(Paragraph(", ".join(missing), styles["BodyText"]))
    else:
        story.append(Paragraph("None", styles["BodyText"]))

    story.append(Paragraph("<b>Suggestions:</b>", styles["Heading2"]))

    for suggestion in suggestions:
        story.append(Paragraph("• " + suggestion, styles["BodyText"]))

    doc.build(story)

    return filename