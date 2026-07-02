from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from strength_checker import check_strength

def generate_report(password):
    result=check_strength(password)
    pdf=SimpleDocTemplate("Password_Audit_Report.pdf")
    styles=getSampleStyleSheet()
    content=[Paragraph("Password Security Audit Report",styles["Title"])]
    for k,v in result.items():
        content.append(Paragraph(f"{k}: {v}",styles["BodyText"]))
    pdf.build(content)
    print("Report Generated")
