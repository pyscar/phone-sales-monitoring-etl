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

![Executive](dashboard/Executive%20Dashboard%201.png)

---

## Branch Performance

![Branch](dashboard/Branch%20Performance%202.png)

---

## Sales & Agent Performance

![Sales](dashboard/Sales%20%26%20Agent%20Performance%203.png)

---

## Product Performance

![Product](dashboard/Product%20Performance%20%26%20Loan%20Health%204.png)

---

## Audit Dashboard

![Audit](dashboard/Audit%20%26%20Reconciliation%205.png)

---

# Author

Oscar Kiamba

Data Engineering | Business Intelligence | AI