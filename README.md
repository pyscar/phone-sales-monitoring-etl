# 📱 Phone Sales Monitoring ETL & Power BI Dashboard

An end-to-end Data Engineering and Business Intelligence project developed to monitor multi-branch phone financing businesses.

The project automates data extraction, cleaning, reconciliation, fraud detection, and dashboard reporting using Python and Power BI.

---

# Project Overview

Many phone retailers sell devices through loan financing.

The challenge is that branch sales, financing records, and head office sales are often stored separately.

This project reconciles these datasets to answer questions such as:

- Which phones were sold but never financed?
- Which loans have no recorded sale?
- Which branches perform best?
- Which agents generate the highest revenue?
- Which brands sell the most?
- How much outstanding debt exists?
- Which transactions require investigation?

---

# Features

✔ Automated ETL Pipeline

✔ Data Cleaning

✔ Data Validation

✔ Loan Reconciliation

✔ Fraud Detection

✔ Executive KPIs

✔ Branch Performance Analysis

✔ Product Performance Analysis

✔ Agent Performance Dashboard

✔ Audit Dashboard

---

# Tech Stack

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Power BI
- Git
- GitHub

---

# Project Structure

```
Phone Sales Monitoring Project

├── data
│
├── notebooks
│
├── src
│   ├── extract
│   ├── transform
│   ├── reconcile
│   ├── load
│   └── pipeline.py
│
├── dashboard
│
├── powerbi
│
└── README.md
```

---

# ETL Workflow

```
Raw Excel Files

        │

        ▼

Extract

        ▼

Transform

        ▼

Reconciliation

        ▼

Export Clean CSV

        ▼

Power BI Dashboard
```

---

# Dashboards

## Executive Dashboard

Provides an executive summary of:

- Revenue
- Phones Sold
- Outstanding Debt
- Average DPD
- Top Branch
- Top Agent

---

## Branch Performance

Compares

- Revenue
- Loans
- Debt
- DPD

across all branches.

---

## Sales & Agent Performance

Shows

- Top Sales Agents
- Revenue by Agent
- Profit by Agent

---

## Product Performance

Shows

- Brand Performance
- Model Performance
- Loan Distribution
- Debt Analysis

---

## Audit Dashboard

Designed for fraud detection.

Highlights

- Sales without matching loans
- Loans without recorded sales
- High debt accounts
- High DPD customers

---

# Future Improvements

- PostgreSQL Integration
- FastAPI Backend
- Automated Scheduling
- AI Business Assistant
- Machine Learning Risk Prediction
- Web Dashboard
- Cloud Deployment

---

# Dashboard Preview

## Executive Dashboard

<img width="1313" height="797" alt="executive_dashboard" src="https://github.com/user-attachments/assets/73bd17a9-853a-4bc1-ab92-b1a89f6a9061" />


---

## Branch Performance
<img width="1315" height="799" alt="branch_performance" src="https://github.com/user-attachments/assets/2645caad-569c-4502-a743-223adb836660" />


---

## Sales & Agent Performance

<img width="1319" height="794" alt="sales_agent_performance" src="https://github.com/user-attachments/assets/78f31db3-91f8-4c4c-af74-5838d22ac36e" />


---

## Product Performance

<img width="1314" height="739" alt="product_performance" src="https://github.com/user-attachments/assets/1ed7eea5-fe77-4df9-a614-cd0a12054345" />


---

## Audit Dashboard

<img width="1319" height="799" alt="audit_dashboard" src="https://github.com/user-attachments/assets/30054296-f891-4454-9556-6ab491c65208" />

---

# Author

Oscar Kiamba

Data Engineering | Business Intelligence | AI
