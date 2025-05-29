"""
Quantitative Trading Strategy Backtesting Platform
=========================================================
This module contains the functionality for error handling.
"""

from typing import Optional


class LoadSaveError(Exception):
    """Loading and saving error class.

    Args:
        message (str, None): Error message. Defaults to None.
    """

    def __init__(self, message: Optional[str] = None) -> None:
        if not message:
            message = "A loading/saving error has occurred."
        self.message = message
        super().__init__(message)
