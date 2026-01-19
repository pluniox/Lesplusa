from __future__ import annotations

from typing import Any

import plotly.graph_objects as go

THEME: dict[str, Any] = {
    "template": "plotly_dark",
    "bg_color": "#0b1220",
    "text": "#f2f5ff",
    "muted": "#a9b1c7",
    "grid": "rgba(255,255,255,0.08)",
    "accent": "#4DA3FF",
    "font": "Inter, sans-serif",
}


def apply_polish(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        template=THEME["template"],
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": THEME["text"], "family": THEME["font"], "size": 13},
        margin={"t": 44, "l": 10, "r": 10, "b": 10},
        title={"x": 0.02, "xanchor": "left"},
        title_font={"size": 16},
    )
    fig.update_xaxes(showgrid=False, zeroline=False, ticks="", tickfont={"color": THEME["muted"]})
    fig.update_yaxes(
        showgrid=True,
        gridcolor=THEME["grid"],
        zeroline=False,
        ticks="",
        tickfont={"color": THEME["muted"]},
    )
    return fig

