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
        annotations=[
            {
                "text": "Pas de données",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 14, "color": THEME["muted_text"]},
            }
        ],
    )
    return apply_polish(fig)


def density_map(df: pd.DataFrame) -> go.Figure:
    if df.empty:
        return blank_figure("Carte de densité")

    fig = px.density_mapbox(
        df,
        lat="lat",
        lon="long",
        radius=14,
        hover_data={"severity_label": True, "lighting_group": True},
        zoom=5,
        center={"lat": 46.6, "lon": 2.5},
        mapbox_style="carto-darkmatter",
        title="CARTE DE CHALEUR",
        color_continuous_scale=THEME["neon_colors"],
    )
    fig.update_layout(margin={"t": 40, "l": 0, "r": 0, "b": 0}, coloraxis_showscale=False)
    return fig


def lighting_pie(df: pd.DataFrame) -> go.Figure:
    if df.empty:
        return blank_figure("Éclairage")
    grouped = df.groupby("lighting_group").size().reset_index(name="accidents")
    fig = px.pie(
        grouped,
        values="accidents",
        names="lighting_group",
        title="ÉCLAIRAGE",
        color_discrete_sequence=THEME["neon_colors"],
        hole=0.55,
    )
    fig.update_traces(textposition="inside", textinfo="percent")
    return apply_polish(fig)


def severity_histogram(df: pd.DataFrame) -> go.Figure:
    if df.empty:
        return blank_figure("Gravité")
    grouped = df["severity_label"].value_counts().reset_index()
    grouped.columns = ["severity_label", "accidents"]
    fig = px.bar(
        grouped,
        x="severity_label",
        y="accidents",
        title="GRAVITÉ",
        color="severity_label",
        color_discrete_sequence=THEME["neon_colors"],
    )
    fig.update_layout(showlegend=False)
    return apply_polish(fig)


def hourly_bar(df: pd.DataFrame) -> go.Figure:
    working = df.dropna(subset=["hour"])
    if working.empty:
        return blank_figure("Distribution horaire")
    grouped = working.groupby("hour").size().reset_index(name="accidents").sort_values("hour")
    fig = px.bar(grouped, x="hour", y="accidents", title="DISTRIBUTION HORAIRE")
    fig.update_traces(marker_color=THEME["neon_colors"][2])
    fig.update_xaxes(dtick=2)
    return apply_polish(fig)

