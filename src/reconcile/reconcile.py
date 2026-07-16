"""
Reconcile Sales and Loan datasets
---------------------------------
Creates reconciliation reports for fraud detection.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd


def reconcile(
    sales: pd.DataFrame,
    loans: pd.DataFrame
):

    sales = sales.copy()
    loans = loans.copy()

    # -------------------------------------------------
    # Standardize IMEI
    # -------------------------------------------------

    sales["serials"] = (
        sales["serials"]
        .astype(str)
        .str.replace(".0", "", regex=False)
        .str.strip()
    )

    loans["imei"] = (
        loans["imei"]
        .astype(str)
        .str.replace(".0", "", regex=False)
        .str.strip()
    )

    # -------------------------------------------------
    # Sales Reconciliation
    # -------------------------------------------------

    sales_reconciliation = sales.merge(
        loans,
        left_on="serials",
        right_on="imei",
        how="left",
        indicator=True
    )

    # Remove duplicate column names created by merge
    sales_reconciliation = sales_reconciliation.loc[
        :,
        ~sales_reconciliation.columns.duplicated()
    ]

    sales_reconciliation["status"] = (
        sales_reconciliation["_merge"]
        .map({
            "both": "Matched",
            "left_only": "Sale Missing Loan"
        })
    )

    # -------------------------------------------------
    # Sales Missing Loan
    # -------------------------------------------------

    sales_not_in_loans = sales_reconciliation[
        sales_reconciliation["_merge"] == "left_only"
    ].copy()

    # -------------------------------------------------
    # Loans Missing Sale
    # -------------------------------------------------

    loan_check = loans.merge(
        sales,
        left_on="imei",
        right_on="serials",
        how="left",
        indicator=True
    )

    loans_not_in_sales = loan_check[
        loan_check["_merge"] == "left_only"
    ].copy()

    # Remove duplicate column names
    loans_not_in_sales = loans_not_in_sales.loc[
        :,
        ~loans_not_in_sales.columns.duplicated()
    ]

    # -------------------------------------------------
    # Enterprise Audit Table
    # -------------------------------------------------

        # -------------------------------------------------
    # Build Enterprise Audit Table
    # -------------------------------------------------

    audit_sales = pd.DataFrame({
        "status": sales_reconciliation["status"],
        "serials": sales_reconciliation["serials"],
        "agreement_number": sales_reconciliation["agreement_number"],
        "branch": sales_reconciliation["branch"],
        "agent_name": sales_reconciliation["agent_name"],
        "brand": sales_reconciliation["brand"],
        "sp": sales_reconciliation["sp"],
        "loan_amount": sales_reconciliation["loan_amount"],
        "debt": sales_reconciliation["debt"],
        "dpd": sales_reconciliation["dpd"]
    })

    audit_loans = pd.DataFrame({
        "status": "Loan Missing Sale",
        "serials": loans_not_in_sales["imei"],
        "agreement_number": loans_not_in_sales["agreement_number"],
        "branch": loans_not_in_sales["shop"],
        "agent_name": loans_not_in_sales["agent"],
        "brand": loans_not_in_sales["brand"],
        "sp": None,
        "loan_amount": loans_not_in_sales["loan_amount"],
        "debt": loans_not_in_sales["debt"],
        "dpd": loans_not_in_sales["dpd"]
    })

    audit_reconciliation = pd.concat(
        [audit_sales, audit_loans],
        ignore_index=True
    )

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    print("=" * 50)
    print("RECONCILIATION COMPLETE")
    print("=" * 50)

    print(f"Sales Records : {len(sales)}")
    print(f"Loan Records  : {len(loans)}")
    print()

    print(
        f"Matched Sales      : {(sales_reconciliation['_merge'] == 'both').sum()}"
    )
    print(f"Sales Missing Loan : {len(sales_not_in_loans)}")
    print(f"Loans Missing Sale : {len(loans_not_in_sales)}")
    print(f"Audit Records      : {len(audit_reconciliation)}")

    return (
        sales_reconciliation,
        sales_not_in_loans,
        loans_not_in_sales,
        audit_reconciliation,
    )


if __name__ == "__main__":

    from extract.load_sales import load_sales
    from extract.load_loans import load_loans

    from transform.clean_sales import clean_sales
    from transform.clean_loans import clean_loans

    sales = load_sales("data/raw/sales_details.xlsx")
    loans = load_loans("data/raw")

    sales = clean_sales(sales)
    loans = clean_loans(loans)

    (
        sales_reconciliation,
        sales_missing,
        loans_missing,
        audit_reconciliation,
    ) = reconcile(sales, loans)

    print("\nSales Reconciliation")
    print(sales_reconciliation.head())

    print("\nSales Missing Loan")
    print(sales_missing.head())

    print("\nLoans Missing Sale")
    print(loans_missing.head())

    print("\nAudit Reconciliation")
    print(audit_reconciliation.head())