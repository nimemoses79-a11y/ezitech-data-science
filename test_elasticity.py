
import pandas as pd
import pytest

from price_elasticity import (
    estimate_price_elasticity,
    calculate_projected_demand,
    calculate_projected_revenue
)

def sample_data():
    return pd.DataFrame({
        "product_id": ["P1", "P2", "P3", "P4"],
        "category": ["Laptop", "Laptop", "Phone", "Phone"],
        "price": [100, 200, 300, 400],
        "units_sold": [50, 40, 30, 20]
    })

def test_estimate_price_elasticity():
    elasticity, r_squared = estimate_price_elasticity(sample_data())

    assert isinstance(elasticity, float)
    assert isinstance(r_squared, float)

def test_elasticity_rejects_invalid_input():
    with pytest.raises(TypeError):
        estimate_price_elasticity("invalid")

def test_elasticity_rejects_missing_columns():
    with pytest.raises(ValueError):
        estimate_price_elasticity(pd.DataFrame({"price": [100]}))

def test_projected_demand():
    result = calculate_projected_demand(100, 1.1, -1)

    assert result == pytest.approx(90.90909, rel=1e-4)

def test_projected_demand_rejects_negative_demand():
    with pytest.raises(ValueError):
        calculate_projected_demand(-10, 1.1, -1)

def test_projected_demand_rejects_invalid_multiplier():
    with pytest.raises(ValueError):
        calculate_projected_demand(100, 0, -1)

def test_projected_revenue():
    result = calculate_projected_revenue(100, 100, 1.1, -1)

    assert result == pytest.approx(10000)

def test_projected_revenue_rejects_invalid_price():
    with pytest.raises(ValueError):
        calculate_projected_revenue(-100, 100, 1.1, -1)


def test_elasticity_rejects_empty_dataset():
    with pytest.raises(ValueError, match="Dataset cannot be empty"):
        estimate_price_elasticity(pd.DataFrame(
            columns=["product_id", "category", "price", "units_sold"]
        ))

def test_elasticity_rejects_missing_values():
    df = sample_data()
    df.loc[0, "price"] = None

    with pytest.raises(ValueError, match="missing values"):
        estimate_price_elasticity(df)

def test_elasticity_rejects_non_numeric_values():
    df = sample_data()
    df["price"] = df["price"].astype(object)
    df.loc[0, "price"] = "invalid"

    with pytest.raises(ValueError, match="finite numbers"):
        estimate_price_elasticity(df)

def test_elasticity_rejects_zero_price():
    df = sample_data()
    df.loc[0, "price"] = 0

    with pytest.raises(ValueError, match="greater than zero"):
        estimate_price_elasticity(df)

def test_elasticity_rejects_negative_units_sold():
    df = sample_data()
    df.loc[0, "units_sold"] = -10

    with pytest.raises(ValueError, match="cannot be negative"):
        estimate_price_elasticity(df)

def test_elasticity_rejects_insufficient_positive_demand():
    df = sample_data()
    df.loc[:, "units_sold"] = 0
    df.loc[0, "units_sold"] = 10

    with pytest.raises(ValueError, match="At least two products"):
        estimate_price_elasticity(df)

def test_projected_demand_rejects_non_numeric_input():
    with pytest.raises(ValueError, match="numeric"):
        calculate_projected_demand("invalid", 1.1, -1)

def test_projected_demand_rejects_infinite_input():
    with pytest.raises(ValueError, match="finite"):
        calculate_projected_demand(float("inf"), 1.1, -1)

def test_projected_revenue_rejects_non_numeric_price():
    with pytest.raises(ValueError, match="numeric"):
        calculate_projected_revenue("invalid", 100, 1.1, -1)

