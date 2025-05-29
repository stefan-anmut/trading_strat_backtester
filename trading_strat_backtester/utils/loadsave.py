"""
Quantitative Trading Strategy Backtesting Platform
=========================================================
This module contains the functionality for loading and saving data.
"""

from datetime import datetime
from typing import Optional, Union

import pandas as pd
import yfinance as yf

from trading_strat_backtester.utils.errors import LoadSaveError


def fetch_yahoo_finance_historical_stock_price_data(
    ticker: str,
    start_date: Optional[Union[str, datetime]],
    end_date: Optional[Union[str, datetime]],
    interval: str = "1d",
) -> Optional[pd.DataFrame]:
    """Fetch historical stock price data from Yahoo! Finance, for a given
    ticker and date range.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT').
        start_date (str, datetime, None): Start date in format 'YYYY-MM-DD' or datetime object.
        end_date (str, datetime, None): End date in format 'YYYY-MM-DD' or datetime object.
        interval (str): Data interval. Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo. Defaults to '1d'.

    Returns:
        DataFrame with columns: Open, High, Low, Close, Adj Close, Volume. Returns None if data fetch fails.
    """
    # Create ticker object
    ticker_obj = yf.Ticker(ticker)

    # Fetch historical data
    data = ticker_obj.history(start=start_date, end=end_date, interval=interval)

    if data.empty:
        LoadSaveError(
            f"No data found for ticker '{ticker}' in the specified date range."
        )

    # Reset index to make Date a column
    data.reset_index(inplace=True)

    return data
