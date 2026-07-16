# 📱 Phone Sales Monitoring System
### End-to-End Data Engineering, PostgreSQL & Business Intelligence Project

An enterprise-style data engineering project that automates phone sales reconciliation, fraud detection, business reporting, and executive analytics.

The project extracts raw sales and loan data, cleans and validates records, reconciles transactions, stores the results in PostgreSQL, and visualizes business insights using Power BI.

---

# Project Architecture

```
                Raw Excel Files
                       │
                       ▼
               Python ETL Pipeline
        ┌────────────────────────────┐
        │ Extract                    │
        │ Clean                      │
        │ Validate                   │
        │ Reconcile                  │
        │ Fraud Detection            │
        │ Audit Reporting            │
        └────────────────────────────┘
                       │
          ┌────────────┴─────────────┐
          ▼                          ▼
     PostgreSQL                 CSV Reports
          │
          ▼
      Power BI Dashboard
```

---

# Business Problem

Many phone retailers operate dozens of branches where:

- Sales are recorded separately
- Loan financing is managed independently
- Head office reporting is delayed
- Fraud is difficult to detect

This project reconciles sales and loan datasets to answer critical business questions such as:

- Which phones were sold but never financed?
- Which loans have no corresponding sale?
- Which branches generate the highest revenue?
- Which agents perform best?
- Which products sell the most?
- How much outstanding debt exists?
- Which transactions require investigation?

---

# Features

### ETL Pipeline

- Automated data extraction
- Data cleaning
- Data validation
- Missing value detection
- Data standardization

### Reconciliation

- Sales vs Loan matching
- Sales without loans
- Loans without sales
- Enterprise audit report

### PostgreSQL Integration

- Automated database loading
- Analytics schema
- Enterprise-ready tables

### Business Intelligence

- Executive Dashboard
- Branch Performance
- Agent Performance
- Product Performance
- Audit Dashboard

---

# Technology Stack

### Programming

- Python
- Pandas
- NumPy

### Database

- PostgreSQL
- pgAdmin

### Business Intelligence

- Power BI

### Development

- Git
- GitHub
- Jupyter Notebook

---

# Project Structure

```
Phone Sales Monitoring Project
│
├── dashboard/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── reports/
│
├── notebooks/
│
├── powerbi/
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── reconcile/
│   ├── load/
│   ├── config.py
│   └── pipeline.py
│
└── README.md
```

---

# ETL Workflow

```
Excel Files

      │

      ▼

Extract

      ▼

Transform

      ▼

Validation

      ▼

Reconciliation

      ▼

PostgreSQL

      ▼

Power BI
```

---

# PostgreSQL Tables

The ETL pipeline automatically loads the following tables into PostgreSQL:

| Table | Description |
|--------|-------------|
| sales | Clean sales dataset |
| master_loans | Clean loan dataset |
| sales_reconciliation | Sales matched against loans |
| sales_not_in_loans | Sales without financing |
| loans_not_in_sales | Loans without recorded sales |
| audit_reconciliation | Enterprise audit report |

---

# Dashboards

## Executive Dashboard

Provides an executive overview of:

- Revenue
- Phones Sold
- Outstanding Debt
- Average DPD
- Top Branch
- Top Agent

---

## Branch Performance

Compares branch performance using:

- Revenue
- Loans
- Debt
- Average DPD

---

## Sales & Agent Performance

Shows:

- Revenue by Agent
- Profit by Agent
- Top Performing Agents

---

## Product Performance

Provides insights into:

- Brand Performance
- Model Performance
- Loan Distribution
- Outstanding Debt

---

## Audit Dashboard

Supports fraud detection by identifying:

- Sales without matching loans
- Loans without sales
- High debt customers
- High DPD accounts
- Transactions requiring investigation

---

# Dashboard Preview

## Executive Dashboard

<img width="1313" height="797" alt="executive_dashboard" src="https://github.com/user-attachments/assets/73bd17a9-853a-4bc1-ab92-b1a89f6a9061"/>

---

## Branch Performance

<img width="1315" height="799" alt="branch_performance" src="https://github.com/user-attachments/assets/2645caad-569c-4502-a743-223adb836660"/>

---

## Sales & Agent Performance

<img width="1319" height="794" alt="sales_agent_performance" src="https://github.com/user-attachments/assets/78f31db3-91f8-4c4c-af74-5838d22ac36e"/>

---

## Product Performance

<img width="1314" height="739" alt="product_performance" src="https://github.com/user-attachments/assets/1ed7eea5-fe77-4df9-a614-cd0a12054345"/>

---

## Audit Dashboard

<img width="1319" height="799" alt="audit_dashboard" src="https://github.com/user-attachments/assets/30054296-f891-4454-9556-6ab491c65208"/>

---

# Future Roadmap

## Version 2 (Current)

- ✅ Python ETL Pipeline
- ✅ PostgreSQL Integration
- ✅ Power BI Dashboard
- ✅ Fraud Detection
- ✅ Audit Reporting

## Version 3

- FastAPI Backend
- REST API
- PostgreSQL Live Queries

## Version 4

- React Dashboard
- Authentication
- Interactive Analytics

## Version 5

- AI Business Assistant
- Natural Language Queries
- Automated Business Insights
- Intelligent Fraud Detection
- LLM-powered Analytics

---

# Author

**Oscar Kiamba**

Data Engineering • Business Intelligence • Artificial Intelligence

GitHub: https://github.com/pyscar
