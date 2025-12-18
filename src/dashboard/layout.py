from __future__ import annotations

import pandas as pd
import plotly.express as px
from dash import dcc, html  # type: ignore


def create_layout(dataframe: pd.DataFrame) -> html.Div:
    fig = px.bar(
        dataframe,
        x="mois",
        y="accidents",
        title="Accidents par mois",
    )
    return html.Div(
        style={"maxWidth": "1100px", "margin": "32px auto", "fontFamily": "Arial"},
        children=[
            html.H1("Dashboard"),
            dcc.Graph(figure=fig),
        ],
    )

