"""
Extract Sales Dataset
---------------------
Loads the raw sales Excel file.
"""

from pathlib import Path
import pandas as pd


def load_sales(file_path: str) -> pd.DataFrame:
    """
    Load sales Excel file.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    pandas.DataFrame
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Sales file not found:\n{file_path}"
        )

    try:
        sales = pd.read_excel(file_path)

        print("=" * 50)
        print("SALES DATA LOADED")
        print("=" * 50)
        print(f"Rows    : {sales.shape[0]}")
        print(f"Columns : {sales.shape[1]}")
        print()

        return sales

    except Exception as e:
        raise Exception(
            f"Unable to load sales file.\n{e}"
        )


if __name__ == "__main__":

    sales = load_sales("data/raw/sales_details.xlsx")

    print(sales.head())