import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('Person.csv')
df2 = pd.read_csv('PersonDemographics.csv')
df3 = pd.read_csv('DegreeConferrals-Table 1.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select DataFrame:"),
        dcc.Dropdown(
            id='dropdown-df',
            options=[
                {'label': 'Person', 'value': 'df1'},
                {'label': 'Person Demographics', 'value': 'df2'},
                {'label': 'Degree Conferrals', 'value': 'df3'}
            ],
            value='df1'
        )
    ]),
    html.Div([
        html.Label("Select X Value:"),
        dcc.Dropdown(id='dropdown-x')
    ]),
    html.Div([
        html.Label("Select Y Value:"),
        dcc.Dropdown(id='dropdown-y')
    ]),
    html.Div([
        html.Label("Select Graph Type:"),
        dcc.Dropdown(
            id='dropdown-graph',
            options=[
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Line Plot', 'value': 'line'},
                {'label': 'Bar Plot', 'value': 'bar'}
            ],
            value='scatter'
        )
    ]),
    dcc.Graph(id='graph')
])

@app.callback(
    [Output('dropdown-x', 'options'),
     Output('dropdown-y', 'options')],
    [Input('dropdown-df', 'value')]
)
def update_dropdowns(selected_df):
    if selected_df == 'df1':
        df = df1
    elif selected_df == 'df2':
        df = df2
    else:
        df = df3
    
    options = [{'label': col, 'value': col} for col in df.columns]
    return options, options

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='dropdown-df', component_property='value'),
     Input(component_id='dropdown-x', component_property='value'),
     Input(component_id='dropdown-y', component_property='value'),
     Input(component_id='dropdown-graph', component_property='value')]
)
def update_graph(selected_df, selected_x, selected_y, selected_graph):
    if selected_df == 'df1':
        df = df1
    elif selected_df == 'df2':
        df = df2
    else:
        df = df3
    
    if selected_graph == 'scatter':
        fig = px.scatter(df, x=selected_x, y=selected_y, title='Scatter Plot')
    elif selected_graph == 'line':
        fig = px.line(df, x=selected_x, y=selected_y, title='Line Plot')
    else:
        fig = px.bar(df, x=selected_x, y=selected_y, title='Bar Plot')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
