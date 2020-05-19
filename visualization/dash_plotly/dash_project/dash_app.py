import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from generate_df import generate_df

df = generate_df()

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dbc.Row([
        dbc.Col(children=[
            dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': f"Group {i}", 'value': i} for i in range(6)],
                value='Group'
            )
        ]),
    ]),
    dbc.Row([
        dbc.Col(children=[html.Div(dcc.Graph(id='plot-1'))], md=5),
        dbc.Col(children=[html.Div(dcc.Graph(id='plot-2'))], md=7)
    ])
])


@app.callback(
    Output("plot-2", "figure"),
    [Input('dropdown-1', 'value')]
)
def update_graph(dropdown_var):
    if dropdown_var:
        df2 = df[df["group"] == dropdown_var].copy()
    else:
        df2 = df.copy()
    fig = go.Figure(
        data=[
            go.Histogram(x=df2["test_0"])
        ]
    )
    fig.update_layout(
        xaxis=dict(title="Test score")
    )
    return fig


@app.callback(
    Output('plot-1', 'figure'),
    [Input('dropdown-1', 'value')]
)
def update_graph(dropdown_var):
    if dropdown_var:
        df2 = df[df["group"] == dropdown_var].copy()
    else:
        df2 = df.copy()
    df2 = df2.groupby("passed").agg({"name": "count"}).reset_index()
    df2['passed'] = df2['passed'].apply(lambda x: 'passed' if x else "failed")
    fig = go.Figure(data=[
        go.Pie(
            name='Passed', values=df2['name'], labels=df2['passed'], textinfo='label+value+percent', 
            hole=.3, marker=dict(colors=["#dd0066", "#0b9822"], line=dict(color="#FFFFFF", width=4))
        )
    ])
    fig.update_layout(
        title="Passed / failed"
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
