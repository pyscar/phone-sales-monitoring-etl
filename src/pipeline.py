"""
Phone Sales ETL Pipeline
------------------------
Runs the complete ETL process from raw files
to cleaned CSVs ready for Power BI.
"""

from extract.load_sales import load_sales
from extract.load_loans import load_loans

from transform.clean_sales import clean_sales
from transform.clean_loans import clean_loans

from reconcile.reconcile import reconcile

from load.export_csv import export_csv


def run_pipeline():

    print("=" * 60)
    print("PHONE SALES ETL PIPELINE")
    print("=" * 60)

    # ---------------------------------
    # Extract
    # ---------------------------------

    sales = load_sales("data/raw/sales_details.xlsx")
    loans = load_loans("data/raw")

    # ---------------------------------
    # Transform
    # ---------------------------------

    sales = clean_sales(sales)
    loans = clean_loans(loans)

    # ---------------------------------
    # Reconcile
    # ---------------------------------

    master, sales_missing, loans_missing = reconcile(
        sales,
        loans
    )

    # ---------------------------------
    # Load
    # ---------------------------------

    export_csv(
        sales,
        "sales_details_clean.csv"
    )

    export_csv(
        loans,
        "master_loans.csv"
    )

    export_csv(
        sales_missing,
        "sales_not_in_loans.csv"
    )

    export_csv(
        loans_missing,
        "loans_not_in_sales.csv"
    )

    export_csv(
        master,
        "master_reconciliation.csv"
    )

    print()
    print("=" * 60)
    print("PIPELINE FINISHED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()