"""
Load Stage
----------
Export processed datasets to CSV.
"""

from pathlib import Path


def export_csv(df, filename):
    """
    Save DataFrame to data/cleaned
    """

    output_folder = Path("data/cleaned")
    output_folder.mkdir(exist_ok=True)

    filepath = output_folder / filename

    df.to_csv(filepath, index=False)

    print(f"✓ Saved {filename}")


if __name__ == "__main__":

    import pandas as pd

    df = pd.DataFrame({
        "A":[1,2,3],
        "B":[4,5,6]
    })

    export_csv(df,"test.csv")