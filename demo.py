import pandas as pd
import plotly.express as px 
import dash 
from dash import dcc, html, Dash, callback, Input, Output

app = Dash(__name__)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

h1_style = {"textAlign": "center", "fontSize": 34}


app.layout = html.Div([
    html.H1(children="Title", style=h1_style),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
    ])

@callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')


if __name__ == "__main__":
    app.run(debug=True) ## remove threaded if crashes // dash.plotly.com/minimal-app

