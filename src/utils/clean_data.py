from __future__ import annotations

from functools import lru_cache

import pandas as pd

from config import CLEANED_FILE


@lru_cache
def load_clean_data() -> pd.DataFrame:
    return pd.read_csv(CLEANED_FILE, parse_dates=["date"])

