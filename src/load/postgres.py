"""
PostgreSQL Loader
-----------------
Loads cleaned datasets into PostgreSQL.
"""

from sqlalchemy import create_engine
from config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def test_connection():
    """
    Test PostgreSQL connection.
    """
    try:
        with engine.connect():
            print("=" * 50)
            print("CONNECTED TO POSTGRESQL")
            print("=" * 50)

    except Exception as e:
        print(e)


def save_dataframe(df, table_name):
    """
    Save a DataFrame into PostgreSQL.
    """

    try:
        df.to_sql(
            name=table_name,
            con=engine,
            schema="analytics",
            if_exists="replace",
            index=False,
        )

        print(f"✓ Loaded {len(df)} rows into analytics.{table_name}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_connection()