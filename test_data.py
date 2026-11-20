import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_integer_dtype,
    is_string_dtype
)

def test_sales_data_exists():
    df = pd.read_csv("sales_data.csv")
    assert not df.empty

def test_correct_columns():
    df = pd.read_csv("sales_data.csv")

    expected_columns = [
        "product_id",
        "category",
        "price",
        "units_sold",
        "date"
    ]

    assert list(df.columns) == expected_columns

def test_dataset_has_50_products_for_365_days():
    df = pd.read_csv("sales_data.csv")

    assert len(df) == 18250
    assert df["product_id"].nunique() == 50
    assert df["date"].nunique() == 365

def test_no_missing_values():
    df = pd.read_csv("sales_data.csv")
    assert df.isnull().sum().sum() == 0

def test_prices_are_valid():
    df = pd.read_csv("sales_data.csv")
    assert (df["price"] >= 0).all()

def test_units_sold_are_valid():
    df = pd.read_csv("sales_data.csv")
    assert (df["units_sold"] >= 0).all()

def test_column_data_types():
    df = pd.read_csv("sales_data.csv")

    # Check text columns
    assert is_string_dtype(df["product_id"])
    assert is_string_dtype(df["category"])

    # Check numeric columns
    assert is_numeric_dtype(df["price"])
    assert is_integer_dtype(df["units_sold"])

    # Check date column
    assert is_string_dtype(df["date"])

    parsed_dates = pd.to_datetime(
        df["date"], errors="coerce"
    )

    assert parsed_dates.notna().all()