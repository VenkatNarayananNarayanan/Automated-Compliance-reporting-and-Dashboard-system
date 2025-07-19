# Automated Compliance Reporting and Dashboard System

A data-driven simulation project that automates compliance violation detection, scoring, dashboarding, and manager reporting — using Alteryx, Tableau, Python, and Windows Task Scheduler.

---

## 📌 Purpose

To eliminate manual compliance checks by automating:
- Rule-based violation detection
- Weekly reporting
- Manager notifications
- Audit logging

This solution enables fast, reliable, and transparent decision-making in regulated environments.

---

## 📂 Dataset

> **Note**: This project uses a **mock dataset** designed specifically for simulation purposes.

The dataset was created with help from ChatGPT to simulate realistic account behavior. It includes:

- ✅ 20% of KYC dates older than 1 year (non-compliant)
- ✅ 25% of payments overdue by more than 60 days
- ✅ 30% of accounts exceeding their credit limit
- ✅ 15 “Delinquent” and 10 “Watchlist” statuses
- ✅ Balanced variations across regions and risk levels

The dataset structure mirrors what you’d expect in a real financial institution’s account monitoring table. No real customer or proprietary data is used.

---

## ⚙️ Tools Used

- **Alteryx Designer**: Data cleaning, compliance rule logic, risk scoring, and automation workflows
- **Tableau Public**: Interactive dashboards for violations, time trends, drill-downs, and audit panels
- **Python**: Email automation (SMTP) and audit log file generation
- **Windows Task Scheduler**: Weekly automation for .py and .bat executions

---

## 🧠 Key Features

### ✅ Rule-Based Detection
- Flags accounts for:
  - KYC outdated
  - Over-limit balances
  - Late payments
  - Risky statuses like "Delinquent" or "Watchlist"

### 🔢 Compliance Risk Scoring
- Weighted scores by rule severity
- Enables account prioritization in Tableau

### 💬 Violation Explanation Panel
- Shows why each account was flagged (e.g., `KYC outdated, Overlimit`)

### 📊 Tableau Dashboards
- **Dashboard 1**: Compliance Overview
- **Dashboard 2**: Drill-Down Risk Explorer
- **Dashboard 3**: Time Trends for KYC, Late Payments, Violations

### 📂 Audit Trail Panel
- Tracks PDF report exports
- Shows file name and timestamp inside Tableau

### 📧 Weekly Manager Email
- Python script sends the most PDF report from `/report` folder
- Integrated with Gmail via App Password for secure SMTP

---

## 🔜 Future Enhancements

- 📌 Anomaly Detection using IQR or Isolation Forest
- 📩 Email delivery logs for report confirmation
- 🧠 Visual logic builder for rule creation
- 🗂️ Auto-archiving reports by date for regulatory audits

---

# Screenshots Folder includes

| No. | File Name                                     | Image Description                  |
| --- | --------------------------------------------- | ---------------------------------- |
| 1   | `Alteryx Workflow.png`                        | Alteryx ETL pipeline               |
| 2   | `Compliance dashboard.png`                    | Tableau: Compliance Dashboard      |
| 3   | `risk explor table.png`                       | Tableau: Risk Explorer Table       |
| 4   | `Time trend.png`                              | Tableau: KYC/Violation Trends      |
| 5   | `Before Automate Weekly compliance task.png`  | Before automation compliance proof |
| 6   | `After Automated weekly compliance task .png` | After automation compliance result |
| 7   | `After Audit report generated.png`            | Audit log file CSV updated         |
| 8   | `Audit Panel.png`                             | Tableau: Audit Trail panel         |
| 9   | `Automated email to manager.png`              | Screenshot of email with reports   |
