"""
Utility functions used throughout the ETL pipeline.
"""

import pandas as pd


def standardize_columns(df):
    """
    Standardize dataframe column names.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("-", "_")
        .str.replace("<", "less_than")
        .str.replace(">", "greater_than")
    )

    return df


def remove_extra_spaces(df):
    """
    Remove leading/trailing spaces from text columns.
    """

    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:
        df[col] = df[col].astype(str).str.strip()

    return df