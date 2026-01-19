from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.dashboard.theme import THEME, apply_polish


def blank_figure(title: str) -> go.Figure:
    fig = px.scatter()
    fig.update_layout(
        title=title,
        xaxis={"visible": False},
        yaxis={"visible": False},
        annotations=[{"text": "Pas de données", "xref": "paper", "yref": "paper", "showarrow": False}],
    )
    return apply_polish(fig)


def severity_histogram(df: pd.DataFrame) -> go.Figure:
    if df.empty:
        return blank_figure("Gravité")
    grouped = df["severity_label"].value_counts().reset_index()
    grouped.columns = ["severity_label", "accidents"]
    fig = px.bar(grouped, x="severity_label", y="accidents", title="GRAVITÉ")
    fig.update_traces(marker_color=THEME["accent"])
    return apply_polish(fig)


def hourly_bar(df: pd.DataFrame) -> go.Figure:
    working = df.dropna(subset=["hour"])
    if working.empty:
        return blank_figure("Distribution horaire")
    grouped = working.groupby("hour").size().reset_index(name="accidents").sort_values("hour")
    fig = px.bar(grouped, x="hour", y="accidents", title="DISTRIBUTION HORAIRE")
    fig.update_traces(marker_color=THEME["accent"])
    fig.update_xaxes(dtick=2)
    return apply_polish(fig)

