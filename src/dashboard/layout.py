from __future__ import annotations

import pandas as pd
import plotly.express as px
from dash import dcc, html  # type: ignore


def create_layout(dataframe: pd.DataFrame) -> html.Div:
    total = len(dataframe)
    counts = dataframe["severity_label"].value_counts().reset_index()
    counts.columns = ["severity_label", "accidents"]

    fig = px.bar(
        counts,
        x="severity_label",
        y="accidents",
        title="Accidents par gravité (échantillon)",
    )

    return html.Div(
        style={"maxWidth": "1100px", "margin": "32px auto", "fontFamily": "Arial"},
        children=[
            html.H1("ACCIDENTS ROUTIERS"),
            html.Div(
                style={
                    "display": "flex",
                    "gap": "12px",
                    "marginTop": "16px",
                    "marginBottom": "12px",
                },
                children=[
                    html.Div(
                        style={
                            "padding": "12px 16px",
                            "border": "1px solid #ddd",
                            "borderRadius": "10px",
                            "minWidth": "200px",
                        },
                        children=[
                            html.Div("TOTAL ACCIDENTS", style={"fontSize": "12px", "color": "#555"}),
                            html.Div(str(total), style={"fontSize": "28px", "fontWeight": "bold"}),
                        ],
                    )
                ],
            ),
            dcc.Graph(figure=fig),
        ],
    )

