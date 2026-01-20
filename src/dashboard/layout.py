from __future__ import annotations

import pandas as pd
from dash import dcc, html  # type: ignore


def _kpi_card(id_value: str, label_text: str) -> html.Div:
    return html.Div(
        className="kpi-card",
        children=[
            html.Div(label_text, className="kpi-label"),
            html.Div("0", id=id_value, className="kpi-value"),
        ],
    )


def create_layout(dataframe: pd.DataFrame) -> html.Div:
    severities = sorted(dataframe["severity_label"].dropna().unique())
    default_sev = [s for s in severities if s != "Indemne"] or severities

    return html.Div(
        className="container",
        children=[
            html.Div(
                className="header-container",
                children=[
                    html.Div(
                        className="app-title",
                        children=[
                            html.H1("ACCIDENTS ROUTIERS"),
                            html.P(
                                "Étape 07 : + charts (map/pie) avant la version finale.",
                                className="app-subtitle",
                            ),
                        ],
                    )
                ],
            ),
            html.Div(
                className="kpi-grid",
                children=[
                    _kpi_card("kpi-total-val", "TOTAL ACCIDENTS"),
                    _kpi_card("kpi-killed-val", "DÉCÈS"),
                    _kpi_card("kpi-injured-val", "BLESSÉS"),
                ],
            ),
            html.Div(
                className="controls-panel",
                children=[
                    html.Div(
                        className="controls-grid",
                        children=[
                            html.Div(
                                [
                                    html.Label("PÉRIODE"),
                                    dcc.DatePickerRange(
                                        id="date-range",
                                        min_date_allowed="2022-01-01",
                                        max_date_allowed="2022-12-31",
                                        initial_visible_month="2022-01-01",
                                        start_date="2022-01-01",
                                        end_date="2022-12-31",
                                        display_format="DD/MM/YYYY",
                                    ),
                                ],
                                className="control-item",
                            ),
                            html.Div(
                                [
                                    html.Label("GRAVITÉ"),
                                    dcc.Dropdown(
                                        id="severity-filter",
                                        options=[{"label": label, "value": label} for label in severities],
                                        value=default_sev,
                                        multi=True,
                                    ),
                                ],
                                className="control-item",
                            ),
                        ],
                    )
                ],
            ),
            html.Div(
                className="charts-grid",
                children=[
                    html.Div(
                        dcc.Graph(id="density-map", config={"displayModeBar": False}),
                        className="chart-card",
                    ),
                    html.Div(
                        dcc.Graph(id="kpi-pie", config={"displayModeBar": False}),
                        className="chart-card",
                    ),
                    html.Div(
                        dcc.Graph(id="severity-graph", config={"displayModeBar": False}),
                        className="chart-card",
                    ),
                    html.Div(
                        dcc.Graph(id="hourly-graph", config={"displayModeBar": False}),
                        className="chart-card",
                    ),
                ],
            ),
        ],
    )

