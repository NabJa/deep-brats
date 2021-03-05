import pandas as pd
from pathlib import Path
import dash
import dash_core_components as dcc
import dash_html_components as html

from uncertainty.visualisation.interactive import plot_volume_3d
from uncertainty.data import data

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Basic MRI plot

meta_data = pd.read_csv(Path("../../data/meta_data.csv"))

brain, bmask = data.get_volume(1, meta_data)
t1, t1gd, t2, flair = brain[..., 0], brain[..., 1], brain[..., 2], brain[..., 3]

fig = plot_volume_3d(t1)

app.layout = html.Div(
    style={"height": "95vh"},
    children=[
        html.H1(
            "3D Plot of MRI image",
            style={"textAlign": "center"},
        ),
        html.Center(dcc.Graph(figure=fig)),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
