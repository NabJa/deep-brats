import pandas as pd
from pathlib import Path
import dash
import dash_core_components as dcc
import dash_html_components as html

from uncertainty.visualisation.interactive import plot_volume_3d
from uncertainty.data import data


# Basic MRI plot

meta_data = pd.read_csv(Path("../../data/meta_data.csv"))

brain, bmask = data.get_volume(1, meta_data)
t1, t1gd, t2, flair = brain[..., 0], brain[..., 1], brain[..., 2], brain[..., 3]

fig = plot_volume_3d(t1)

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)
