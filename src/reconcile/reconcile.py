"""
Reconcile Sales and Loan datasets
---------------------------------
Creates reconciliation reports for fraud detection.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd


def reconcile(sales: pd.DataFrame,
              loans: pd.DataFrame):
    """
    Compare Sales against Loans using IMEI.
    """

    sales = sales.copy()
    loans = loans.copy()

    # ----------------------------
    # Convert IMEI to string
    # ----------------------------

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

    # ===================================================
    # MASTER TABLE
    # ===================================================

    master = sales.merge(

        loans,

        left_on="serials",

        right_on="imei",

        how="left",

        indicator=True

    )

    # ===================================================
    # SALES WITHOUT LOANS
    # ===================================================

    sales_not_in_loans = master[
        master["_merge"] == "left_only"
    ].copy()

    # ===================================================
    # LOANS WITHOUT SALES
    # ===================================================

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

    print("=" * 50)
    print("RECONCILIATION COMPLETE")
    print("=" * 50)

    print(f"Sales Records : {len(sales)}")
    print(f"Loan Records  : {len(loans)}")

    print()

    print(f"Sales Missing Loan : {len(sales_not_in_loans)}")

    print(f"Loans Missing Sale : {len(loans_not_in_sales)}")

    return (
        master,
        sales_not_in_loans,
        loans_not_in_sales
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

    master, sales_missing, loans_missing = reconcile(
        sales,
        loans
    )

    print()

    print(master.head())

    print()

    print(sales_missing.head())

    print()

    print(loans_missing.head())