import plotly.graph_objects as go
from dash import Dash, dcc, html  # type: ignore


def main() -> None:
    fig = go.Figure(
        data=[
            go.Scatter(
                x=["Lun", "Mar", "Mer", "Jeu", "Ven"],
                y=[12, 9, 14, 7, 11],
                mode="lines+markers",
            )
        ]
    )
    fig.update_layout(title="Premier graphique")

    app = Dash(__name__)
    app.title = "Dashboard"
    app.layout = html.Div(
        style={"maxWidth": "1000px", "margin": "40px auto", "fontFamily": "Arial"},
        children=[
            html.H1("Dashboard"),
            dcc.Graph(figure=fig),
        ],
    )
    app.run(debug=False, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    main()

