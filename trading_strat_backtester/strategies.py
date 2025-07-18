"""
Quantitative Trading Strategy Backtesting Platform
=========================================================
This module contains the functionality for employing different trading strategies.
"""

import pandas as pd


def _calculate_returns(price_s: pd.Series) -> pd.Series:
    """Calculate period-over-period returns from a price series.

    Returns are calculated as: (price_{t} - price_{t-1}) / price_{t-1}
    The first value will be NaN since there's no previous period to compare against.

    Args:
        price_s (pd.Series): A pandas Series of asset prices.

    Returns:
        A pandas Series containing the period-over-period percentage returns.
    """
    return price_s.pct_change()


def _simple_moving_average(price_s: pd.Series, window: int) -> pd.Series:
    """Calculate the simple moving average (SMA) over a specified window.

    Args:
        price_s (pd.Series): A pandas Series of historical stock prices (e.g., closing prices).
        window (int): The number of periods to average over (e.g., 20 for a 20-day SMA).

    Returns:
        A pandas Series representing the SMA.

    Raises:
        ValueError: If the input series is empty or if the window is not a positive integer.
    """
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer.")

    return price_s.rolling(window=window).mean()


def moving_average_crossover_strat(
    price_s: pd.Series, short_window: int = 20, long_window: int = 50
) -> pd.DataFrame:
    strat_df = price_s.copy(deep=True).to_frame(name="Price")

    # Calculate moving averages
    strat_df["SMA_short"] = _simple_moving_average(price_s, window=short_window)
    strat_df["SMA_long"] = _simple_moving_average(price_s, window=long_window)

    # Generates buy/sell signals based on SMA crossovers
    strat_df["Signal"] = 0
    strat_df.loc[strat_df["SMA_short"] > strat_df["SMA_long"], "Signal"] = 1
    strat_df.loc[strat_df["SMA_short"] < strat_df["SMA_long"], "Signal"] = -1
    strat_df["Position"] = strat_df["Signal"].shift(1)

    # Calculate the market returns and the strategy returns
    strat_df["Return"] = _calculate_returns(price_s=price_s)
    strat_df["Strategy_return"] = strat_df["Return"] * strat_df["Position"]

    return strat_df
