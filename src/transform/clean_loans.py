"""
Transform Loan Dataset
----------------------
Clean and standardize all loan datasets.
"""

import sys
from pathlib import Path

# Allow imports from src/
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd


def clean_loans(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the loan dataset.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    loans = df.copy()

    # ----------------------------------
    # Standardize column names
    # ----------------------------------

    loans.columns = (
        loans.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("<", "less_than")
        .str.replace("/", "_")
    )

    # ----------------------------------
    # Dates
    # ----------------------------------

    loans["issuance_date"] = pd.to_datetime(
        loans["issuance_date"],
        errors="coerce"
    )

    # ----------------------------------
    # Text Columns
    # ----------------------------------

    text_columns = [
        "dealer",
        "shop",
        "agent",
        "brand",
        "model",
        "market_name"
    ]

    for col in text_columns:

        loans[col] = (
            loans[col]
            .astype(str)
            .str.upper()
            .str.strip()
        )

    # ----------------------------------
    # Numeric Columns
    # ----------------------------------

    numeric_columns = [
        "loan_amount",
        "phone_price",
        "dpd",
        "debt"
    ]

    for col in numeric_columns:

        loans[col] = (
            loans[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )

        loans[col] = pd.to_numeric(
            loans[col],
            errors="coerce"
        )

    # ----------------------------------
    # IMEI
    # ----------------------------------

    loans["imei"] = (
        loans["imei"]
        .astype(str)
        .str.replace(".0", "", regex=False)
        .str.strip()
    )

    # ----------------------------------
    # Validation Flags
    # ----------------------------------

    loans["missing_debt"] = loans["debt"].isna()

    loans["missing_imei"] = (
        loans["imei"].isna()
        | (loans["imei"] == "")
        | (loans["imei"] == "nan")
    )

    # ----------------------------------
    # Branch Extraction
    # ----------------------------------

    branches = [
        "THIKA",
        "KIAMBU",
        "LOWER KABETE",
        "BUNGOMA",
        "MURANG'A",
        "MOMBASA",
        "KWALE",
        "MALINDI",
        "NANYUKI",
        "MAKONGENI",
        "KITALE",
        "NYERI"
    ]

    loans["branch"] = "OTHER"

    for branch in branches:

        loans.loc[
            loans["shop"].str.contains(branch, case=False, na=False),
            "branch"
        ] = branch

    print("=" * 50)
    print("LOANS CLEANED")
    print("=" * 50)
    print(f"Rows    : {loans.shape[0]}")
    print(f"Columns : {loans.shape[1]}")

    return loans


if __name__ == "__main__":

    from extract.load_loans import load_loans

    loans = load_loans("data/raw")

    loans = clean_loans(loans)

    print(loans.head())