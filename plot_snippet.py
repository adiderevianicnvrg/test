import numpy as np
import dash
import plotly.graph_objects as go
from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True
)

app.layout = html.Div(
    [dcc.Location(id="url"), html.Button("refresh", id="refresh-button"), html.Div(id="timeseries-viewer-graph")],
    style={"align-items": "stretch"},
)

server = app.server


@dash.callback(
    Output("timeseries-viewer-graph", "children"),
    Input("refresh-button", "n_clicks")
)
def render_graph_for_timeseries(n_clicks):
    if not n_clicks:
        return None

    # Spoof the data
    n_of_elements = 30000
    timeseries_variables = np.random.rand(n_of_elements)

    # Get the trace
    timeseries_trace = get_scatterplot_for_trace(
        x=np.arange(len(timeseries_variables)),
        y=timeseries_variables.flatten(),
        line_color="red",
        yaxis="y",
        name="Input time series",
    )

    # Create the figure and add time series traces
    fig = go.Figure(data=[timeseries_trace], layout=get_graph_layout())

    graph = dcc.Graph(figure=fig)
    return graph


def get_graph_layout() -> go.Layout:
    return go.Layout(
        xaxis=dict(anchor="x"),
        yaxis=dict(anchor="y", domain=[0.55, 1.0]),
        yaxis2=dict(anchor="y2", domain=[0.0, 0.45]),
    )


def get_scatterplot_for_trace(
    x: np.ndarray, y: np.ndarray, line_color: str, yaxis: str, name: str, **kwargs
) -> go.Scatter:
    return go.Scatter(
        **kwargs,
        x=x,
        y=y,
        mode="lines+markers",
        line_color=line_color,
        xaxis="x",
        yaxis=yaxis,
        name=name,
    )

if __name__ == "__main__":
    app.run_server(debug=True)