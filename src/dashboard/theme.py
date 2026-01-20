from __future__ import annotations

from typing import Any

import plotly.graph_objects as go

THEME: dict[str, Any] = {
    "template": "plotly_dark",
    "bg_color": "rgba(0,0,0,0)",
    "text_color": "#f2f5ff",
    "muted_text": "#a9b1c7",
    "grid_color": "rgba(255,255,255,0.06)",
    "neon_colors": ["#4DA3FF", "#A855F7", "#06B6D4", "#F43F5E", "#22C55E", "#FBBF24"],
    "font_family": "Inter, sans-serif",
}


def apply_polish(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        template=THEME["template"],
        paper_bgcolor=THEME["bg_color"],
        plot_bgcolor=THEME["bg_color"],
        font={"color": THEME["text_color"], "family": THEME["font_family"], "size": 13},
        margin={"t": 46, "l": 12, "r": 12, "b": 10},
        title={"x": 0.02, "xanchor": "left"},
        title_font={"size": 16, "family": THEME["font_family"]},
    )
    fig.update_xaxes(
        showgrid=False,
        gridcolor=THEME["grid_color"],
        zeroline=False,
        showline=False,
        ticks="",
        tickfont={"color": THEME["muted_text"], "family": THEME["font_family"]},
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor=THEME["grid_color"],
        zeroline=False,
        showline=False,
        ticks="",
        tickfont={"color": THEME["muted_text"], "family": THEME["font_family"]},
    )
    return fig

