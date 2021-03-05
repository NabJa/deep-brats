import plotly.graph_objects as go
import numpy as np


def plot_volume_3d(volume):
    """Generate interactive 3D plot of volume with slider."""

    nslices, width, height = volume.shape
    base_mat = np.ones((height, width))

    def _frame_args(duration):
        return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }

    fig = go.Figure(
        frames=[
            go.Frame(
                data=go.Surface(
                    z=(nslices - i) * base_mat,
                    surfacecolor=volume[nslices - (i + 1)],
                    cmin=volume[nslices - (i + 1)].min(),
                    cmax=volume[nslices - (i + 1)].max(),
                ),
                name=f"Frame {i}",
            )
            for i in range(nslices)
        ]
    )

    # Add data to be displayed before animation starts
    fig.add_trace(
        go.Surface(
            z=nslices * base_mat,
            surfacecolor=volume[nslices - 1],
            colorscale="Gray",
            cmin=volume[nslices - 1].min(),
            cmax=volume[nslices - 1].max(),
            colorbar=dict(thickness=20, ticklen=4),
        )
    )

    sliders = [
        {
            "pad": {"b": 10, "t": 60},
            "len": 0.9,
            "x": 0.1,
            "y": 0,
            "steps": [
                {
                    "args": [[frame.name], _frame_args(0)],
                    "label": str(i),
                    "method": "animate",
                }
                for i, frame in enumerate(fig.frames)
            ],
        }
    ]

    # Layout
    fig.update_layout(
        title="Slices in MRI data",
        width=750,
        height=750,
        scene=dict(
            zaxis=dict(range=[-1, nslices + 1], autorange=False),
            aspectratio=dict(x=1, y=1, z=1),
        ),
        updatemenus=[
            {
                "buttons": [
                    {
                        "args": [None, _frame_args(50)],
                        "label": "&#9654;",  # play symbol
                        "method": "animate",
                    },
                    {
                        "args": [[None], _frame_args(0)],
                        "label": "&#9724;",  # pause symbol
                        "method": "animate",
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 70},
                "type": "buttons",
                "x": 0.1,
                "y": 0,
            }
        ],
        sliders=sliders,
    )

    return fig
