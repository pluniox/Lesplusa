from __future__ import annotations

import pandas as pd
from dash import Dash, Input, Output  # type: ignore

from src.dashboard.charts import density_map, hourly_bar, lighting_pie, severity_histogram
from src.utils.common_functions import filter_dataframe


def register_callbacks(app: Dash, dataframe: pd.DataFrame) -> None:
    @app.callback(
        Output("kpi-total-val", "children"),
        Output("kpi-killed-val", "children"),
        Output("kpi-injured-val", "children"),
        Output("density-map", "figure"),
        Output("kpi-pie", "figure"),
        Output("severity-graph", "figure"),
        Output("hourly-graph", "figure"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
        Input("severity-filter", "value"),
    )
    def update_dashboard(start, end, severities):
        severities = severities or []
        filtered = filter_dataframe(dataframe, date_range=(start, end), severities=severities)

        total = len(filtered)
        killed = int((filtered["severity_label"] == "Tue").sum())
        injured = int(filtered["severity_label"].isin(["Blesse hospitalise", "Blesse leger"]).sum())

        total_str = f"{total:,}".replace(",", " ")
        killed_str = f"{killed:,}".replace(",", " ")
        injured_str = f"{injured:,}".replace(",", " ")

        return (
            total_str,
            killed_str,
            injured_str,
            density_map(filtered),
            lighting_pie(filtered),
            severity_histogram(filtered),
            hourly_bar(filtered),
        )

