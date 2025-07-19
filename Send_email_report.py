#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
import os
from email.message import EmailMessage
from datetime import datetime

# ==== CONFIGURE THESE ====
EMAIL_ADDRESS = "sampleandtestingdata@gmail.com"
EMAIL_PASSWORD = "cbwsolrxiaamahut"
TO_EMAIL = "pythonboyvenky@gmail.com"
REPORT_FOLDER = r"C:\Users\VENKAT\Desktop\Compliance_project\report"
# ==========================

# Compose message
msg = EmailMessage()
msg["Subject"] = f"Weekly Compliance Reports – {datetime.now().strftime('%d-%m-%Y')}"
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg.set_content("Hi Manager,\n\nPlease find attached the latest compliance reports.\n\nRegards,\nCompliance System")

# Attach all PDFs
for filename in os.listdir(REPORT_FOLDER):
    if filename.endswith(".pdf"):
        filepath = os.path.join(REPORT_FOLDER, filename)
        with open(filepath, "rb") as f:
            file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=filename)

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("✅ Email sent successfully.")


# In[ ]:




