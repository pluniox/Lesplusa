from __future__ import annotations

import pandas as pd
from dash import Dash  # type: ignore

from src.dashboard.layout import create_layout


def create_app() -> Dash:
    df = pd.DataFrame(
        {
            "mois": ["Jan", "Fev", "Mar", "Avr", "Mai", "Jun"],
            "accidents": [120, 98, 135, 110, 143, 126],
        }
    )

    app = Dash(__name__)
    app.title = "Dashboard"
    app.layout = create_layout(df)
    return app

