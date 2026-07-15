"""
Transform Sales Dataset
-----------------------
Clean and standardize the sales dataset.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the sales dataset.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    Clean DataFrame
    """

    sales = df.copy()

    # ----------------------------
    # Rename Columns
    # ----------------------------

    sales.columns = (
        sales.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # ----------------------------
    # Dates
    # ----------------------------

    sales["date"] = pd.to_datetime(
        sales["date"],
        dayfirst=True,
        errors="coerce"
    )

    # ----------------------------
    # Company
    # ----------------------------

    sales["company"] = (
        sales["company"]
        .str.upper()
        .str.strip()
    )

    # ----------------------------
    # Customer
    # ----------------------------

    sales["customer_name"] = (
        sales["customer_name"]
        .str.upper()
        .str.strip()
    )

    # ----------------------------
    # Agent Cleaning
    # ----------------------------

    agent = sales["agent"].str.split("|", expand=True)

    sales["agent_name"] = (
        agent[0]
        .str.upper()
        .str.strip()
    )

    sales["agent_phone"] = (
        agent[1]
        .str.strip()
        .str.replace(" ", "", regex=False)
    )

    sales["country"] = (
        agent[2]
        .str.upper()
        .str.strip()
    )

    sales.drop(columns="agent", inplace=True)

    # ----------------------------
    # Numeric Columns
    # ----------------------------

    numeric = [
        "customer_id",
        "customer_phone",
        "serials",
        "bp",
        "sp",
        "margin"
    ]

    for col in numeric:

        sales[col] = pd.to_numeric(
            sales[col],
            errors="coerce"
        )

    # ----------------------------
    # Validation Flags
    # ----------------------------

    sales["missing_customer"] = sales["customer_name"].isna()

    sales["missing_serial"] = sales["serials"].isna()

    sales["missing_agent"] = sales["agent_name"].isna()

    print("=" * 50)
    print("SALES CLEANED")
    print("=" * 50)
    print(f"Rows : {sales.shape[0]}")
    print(f"Columns : {sales.shape[1]}")

    return sales


if __name__ == "__main__":

    from extract.load_sales import load_sales

    sales = load_sales("data/raw/sales_details.xlsx")

    sales = clean_sales(sales)

    print(sales.head())