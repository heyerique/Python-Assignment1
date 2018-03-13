# Vaishali
from View.IGraphView import IGraphView
import plotly
from plotly.graph_objs import Scatter, Layout

plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})

fig = {
    'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
              'values': [19, 26, 55],
              'type': 'pie'}],
    'layout': {
        'title': 'Forcasted 2014 U.S. PV Installations by Market Segment'}
}

plotly.offline.plot(fig)
