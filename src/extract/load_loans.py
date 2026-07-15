"""
Extract Loan Datasets
---------------------
Loads all loan files from the raw folder and combines them
into one DataFrame.
"""

from pathlib import Path
import pandas as pd


def load_loans(folder_path: str) -> pd.DataFrame:
    """
    Load all loan datasets (.xlsx and .csv)
    from the specified folder.

    Parameters
    ----------
    folder_path : str

    Returns
    -------
    pandas.DataFrame
    """

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(
            f"Folder not found:\n{folder}"
        )

    loan_files = list(folder.glob("loan_list*.xlsx"))
    loan_files += list(folder.glob("loan_list*.csv"))

    if not loan_files:
        raise FileNotFoundError(
            "No loan files were found."
        )

    dataframes = []

    print("=" * 50)
    print("LOADING LOAN FILES")
    print("=" * 50)

    for file in loan_files:

        print(f"Loading {file.name}")

        if file.suffix.lower() == ".xlsx":
            df = pd.read_excel(file)

        elif file.suffix.lower() == ".csv":
            df = pd.read_csv(file)

        dataframes.append(df)

    loans = pd.concat(
        dataframes,
        ignore_index=True
    )

    print()
    print("=" * 50)
    print("MASTER LOANS CREATED")
    print("=" * 50)
    print(f"Files Loaded : {len(loan_files)}")
    print(f"Rows         : {loans.shape[0]}")
    print(f"Columns      : {loans.shape[1]}")
    print()

    return loans


if __name__ == "__main__":

    loans = load_loans("data/raw")

    print(loans.head())