import pandas as pd

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

def test_dataset_has_50_records():
    df = pd.read_csv("sales_data.csv")
    assert len(df) == 18250

def test_no_missing_values():
    df = pd.read_csv("sales_data.csv")
    assert df.isnull().sum().sum() == 0

def test_prices_are_positive():
    df = pd.read_csv("sales_data.csv")
    assert (df["price"] > 0).all()

def test_units_sold_are_valid():
    df = pd.read_csv("sales_data.csv")
    assert (df["units_sold"] >= 0).all()