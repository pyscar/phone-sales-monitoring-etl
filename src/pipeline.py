"""
Phone Sales ETL Pipeline
------------------------
Runs the complete ETL process from raw files
to cleaned CSVs and PostgreSQL ready for Power BI.
"""

from extract.load_sales import load_sales
from extract.load_loans import load_loans

from transform.clean_sales import clean_sales
from transform.clean_loans import clean_loans

from reconcile.reconcile import reconcile

from load.export_csv import export_csv
from load.postgres import save_dataframe


def run_pipeline():

    print("=" * 60)
    print("PHONE SALES ETL PIPELINE")
    print("=" * 60)

    # ==================================================
    # EXTRACT
    # ==================================================

    sales = load_sales("data/raw/sales_details.xlsx")
    loans = load_loans("data/raw")

    # ==================================================
    # TRANSFORM
    # ==================================================

    sales = clean_sales(sales)
    loans = clean_loans(loans)

    # ==================================================
    # RECONCILIATION
    # ==================================================

    (
    sales_reconciliation,
    sales_missing,
    loans_missing,
    audit_reconciliation
    ) = reconcile(
    sales,
    loans
    )



    # ==================================================
    # LOAD TO POSTGRESQL
    # ==================================================

    print()
    print("=" * 60)
    print("LOADING DATA INTO POSTGRESQL")
    print("=" * 60)

    save_dataframe(
        sales,
        "sales"
    )

    save_dataframe(
        loans,
        "master_loans"
    )

    save_dataframe(
        sales_reconciliation,
        "sales_reconciliation"
    )

    '''print("\nDuplicate columns:")
    print(sales_reconciliation.columns[sales_reconciliation.columns.duplicated()])

    print("\nAll columns:")
    print(sales_reconciliation.columns.tolist())'''

    save_dataframe(
        sales_missing,
        "sales_not_in_loans"
    )

    save_dataframe(
        loans_missing,
        "loans_not_in_sales"
    )

    save_dataframe(
        audit_reconciliation,
        "audit_reconciliation"
    )

    # ==================================================
    # EXPORT CSV REPORTS
    # ==================================================

    print()
    print("=" * 60)
    print("EXPORTING CSV REPORTS")
    print("=" * 60)

    export_csv(
        sales,
        "sales_details_clean.csv"
    )

    export_csv(
        loans,
        "master_loans.csv"
    )

    export_csv(
        sales_reconciliation,
        "sales_reconciliation.csv"
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
       audit_reconciliation,
       "audit_reconciliation.csv"
    )

    print()
    print("=" * 60)
    print("PIPELINE FINISHED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()