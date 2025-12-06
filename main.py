from dash import Dash, html  # type: ignore


def main() -> None:
    app = Dash(__name__)
    app.title = "Dashboard"
    app.layout = html.Div(
        style={"maxWidth": "900px", "margin": "40px auto", "fontFamily": "Arial"},
        children=[
            html.H1("Dashboard"),
        ],
    )
    app.run(debug=False, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    main()

