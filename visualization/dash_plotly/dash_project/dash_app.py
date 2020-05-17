import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


letters = [let for let in 'abcdefghijklmnopqrstuvwxyz']

def generate_name():
    n1 = np.random.randint(3, 5)
    n2 = np.random.randint(3, 10)
    w1 = ''.join(np.random.choice(letters, n1)).capitalize()
    w2 = ''.join(np.random.choice(letters, n2)).capitalize()
    return f"{w1} {w2}"

K = 250
df = pd.DataFrame({
    'name': [generate_name() for _ in range(K)],
    'test_0': [np.round(100 * i / K + np.random.randint(-5, 5)) for i in range(K)],
    'test_1': [np.round(100 * i / K + np.random.randint(-15, 15)) + 10 for i in range(K)],
    'group': [np.random.randint(6) for _ in range(K)]
})
df.loc[df['test_0'] < 0, 'test_0'] = 0
df.loc[df['test_0'] > 100, 'test_0'] = 100
df.loc[df['test_1'] < 0, 'test_1'] = 0
df.loc[df['test_1'] > 100, 'test_1'] = 100

df['passed'] = df['test_1'].apply(lambda x: x > 40)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown-1',
        options=[{'label': f"Group {i}", 'value': i} for i in range(6)],
        value='Group'
    ),
    html.Hr(),
    dcc.Graph(id='plot-1'),
])


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
    sub_df = df[df["group"] == dropdown_var]
    fig = go.Figure(data=[
        go.Pie(
            name='Passed', values=df2['name'], labels=df2['passed'], textinfo='label+value+percent', 
            hole=.3, marker=dict(colors=["#dd0066", "#0b9822"], line=dict(color="#FFFFFF", width=4))
        )
    ])
    fig.update_layout(
        title = "Passed / failed",
        height=500,
        width=500
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
