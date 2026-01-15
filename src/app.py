from __future__ import annotations

from dash import Dash  # type: ignore

from src.dashboard.layout import create_layout
from src.utils.clean_data import load_clean_data


def create_app() -> Dash:
    dataframe = load_clean_data()

    app = Dash(__name__)
    app.title = "Dashboard"
    app.layout = create_layout(dataframe)
    return app

