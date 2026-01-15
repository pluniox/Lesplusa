from __future__ import annotations

from typing import Optional, Sequence, Tuple

import pandas as pd


def filter_dataframe(
    df: pd.DataFrame,
    date_range: Optional[Tuple[str, str]] = None,
    severities: Optional[Sequence[str]] = None,
) -> pd.DataFrame:
    filtered = df
    if date_range and all(date_range):
        start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered = filtered[(filtered["date"] >= start) & (filtered["date"] <= end)]

    if severities:
        filtered = filtered[filtered["severity_label"].isin(severities)]

    return filtered

