from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

# Create data directory
DATA_DIR = ""
#os.makedirs(DATA_DIR, exist_ok=True)

styles = getSampleStyleSheet()

def create_pdf(filename, content):
    file_path = os.path.join(DATA_DIR, filename)
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    story = []

    for line in content.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)
    print(f"✅ Created {file_path}")

# -------- PDF 1: Company Policy --------
company_policy_text = """
<b>Company Policies and Employee Handbook</b><br/><br/>

<b>1. Introduction</b><br/>
This document outlines the company policies applicable to all full-time and part-time employees.
Employees are expected to read and understand these policies to ensure compliance and smooth operations.<br/><br/>

<b>2. Working Hours</b><br/>
Standard working hours are 9:00 AM to 6:00 PM, Monday to Friday.
Employees are expected to log at least 8 working hours per day, excluding lunch breaks.
Flexible working hours may be allowed with prior manager approval.<br/><br/>

<b>3. Leave Policy</b><br/>
Employees are entitled to 20 paid leaves per calendar year.
Casual leave cannot exceed 2 consecutive days without manager approval.
Unused paid leave cannot be carried forward to the next year.<br/><br/>

<b>4. Remote Work Policy</b><br/>
Employees may work remotely up to 2 days per week.
Remote work requests must be approved in advance.
The employee is responsible for maintaining data security while working remotely.<br/><br/>

<b>5. Code of Conduct</b><br/>
Employees must act professionally and ethically at all times.
Harassment or discrimination of any kind will result in disciplinary action.
Confidential company information must not be disclosed to third parties.<br/><br/>

<b>6. Termination Policy</b><br/>
Either party may terminate employment with 30 days written notice.
Immediate termination may occur in cases of severe misconduct.
"""

create_pdf("company_policy.pdf", company_policy_text)

# -------- PDF 2: Product Terms --------
product_terms_text = """
<b>Product Terms, Conditions, and Refund Policy</b><br/><br/>

<b>1. Overview</b><br/>
This document describes the terms and conditions governing the use of the company’s software
products and services.<br/><br/>

<b>2. Subscription Plans</b><br/>
Monthly and annual subscription plans are available.
Subscription fees are charged in advance.
Failure to pay may result in suspension of services.<br/><br/>

<b>3. Usage Limitations</b><br/>
Users must not attempt to reverse engineer the software.
The product may not be resold without written consent.
Fair usage policies apply to API usage.<br/><br/>

<b>4. Refund Policy</b><br/>
Customers may request a refund within 30 days of purchase.
Refunds are applicable only if the product has not been extensively used.
Refund requests must be submitted through the official support channel.
Approved refunds will be processed within 7 to 10 business days.<br/><br/>

<b>5. Data Privacy</b><br/>
Customer data is stored securely and encrypted at rest.
Data will not be shared with third parties without consent.
Users may request data deletion by contacting support.<br/><br/>

<b>6. Support and Escalation</b><br/>
Standard support is available via email during business hours.
Critical issues will be prioritized based on severity level.
"""

create_pdf("product_terms.pdf", product_terms_text)
