#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
from datetime import datetime

# Folder where reports are saved
report_folder = r"C:\Users\VENKAT\Desktop\Compliance_project\report"

# Output audit file path
audit_log_file = os.path.join(report_folder, "report_audit_log.csv")

# Scan the folder for PDFs
files = [f for f in os.listdir(report_folder) if f.endswith(".pdf")]

# Prepare audit log data
audit_data = []
for filename in files:
    try:
        # Extract date and report type from file name
        base = filename.replace(".pdf", "")
        if "_" in base:
            report_name = base.rsplit("_", 1)[0].replace("_", " ")
            date_str = base.rsplit("_", 1)[1]
            gen_date = datetime.strptime(date_str, "%d-%m-%Y")
            audit_data.append([report_name.strip().title(), gen_date.strftime("%Y-%m-%d"), filename])
    except:
        continue  # skip if format is wrong

# Sort by date (newest first)
audit_data.sort(key=lambda x: x[1], reverse=True)

# Write CSV
with open(audit_log_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Report_Name", "Generated_On", "File_Name"])
    writer.writerows(audit_data)

print("✅ Audit log updated:", audit_log_file)


# In[ ]:




