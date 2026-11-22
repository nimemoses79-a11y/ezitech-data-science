
"""Price elasticity estimation and demand forecasting."""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def estimate_price_elasticity(df):
    """Estimate price elasticity using log-log regression."""

    required = {"product_id", "category", "price", "units_sold"}

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    data = df[list(required)].copy()

    if data.isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    for column in ["price", "units_sold"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    if not np.isfinite(data[["price", "units_sold"]]).all().all():
        raise ValueError("Price and demand must be finite numbers.")

    if (data["price"] <= 0).any():
        raise ValueError("Prices must be greater than zero.")

    if (data["units_sold"] < 0).any():
        raise ValueError("Units sold cannot be negative.")

    products = (
        data.groupby(
            ["product_id", "category", "price"],
            as_index=False
        )["units_sold"]
        .mean()
        .rename(columns={"units_sold": "avg_units"})
    )

    # Remove products with zero average demand.
    products = products[products["avg_units"] > 0].copy()

    if len(products) < 2:
        raise ValueError(
            "At least two products with positive average demand are required."
        )

    X = pd.concat(
        [
            np.log(products[["price"]]).rename(
                columns={"price": "log_price"}
            ),
            pd.get_dummies(
                products["category"],
                drop_first=True,
                dtype=float
            )
        ],
        axis=1
    )

    y = np.log(products["avg_units"])

    model = LinearRegression()
    model.fit(X, y)

    return float(model.coef_[0]), float(model.score(X, y))

def calculate_projected_demand(
    base_demand,
    price_multiplier,
    elasticity
):
    """Calculate projected demand using constant elasticity."""

    try:
        base_demand, price_multiplier, elasticity = map(
            float, [base_demand, price_multiplier, elasticity]
        )
    except (TypeError, ValueError):
        raise ValueError("All inputs must be numeric.")

    if not all(np.isfinite(v) for v in [
        base_demand, price_multiplier, elasticity
    ]):
        raise ValueError("Inputs must be finite numbers.")

    if base_demand < 0:
        raise ValueError("Base demand cannot be negative.")

    if price_multiplier <= 0:
        raise ValueError("Price multiplier must be greater than zero.")

    return float(base_demand * price_multiplier ** elasticity)

def calculate_projected_revenue(
    base_price,
    base_demand,
    price_multiplier,
    elasticity
):
    """Calculate projected revenue after a price adjustment."""

    try:
        base_price = float(base_price)
    except (TypeError, ValueError):
        raise ValueError("Base price must be numeric.")

    if not np.isfinite(base_price) or base_price <= 0:
        raise ValueError("Base price must be finite and positive.")

    demand = calculate_projected_demand(
        base_demand,
        price_multiplier,
        elasticity
    )

    return float(base_price * price_multiplier * demand)