import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    'log.csv', header=None)
rows_global=len(df);

#available_indicators = df['Indicator Name'].unique()

app.layout = html.Div([
    
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'freq1', 'value': 1 }, {'label': 'freq2', 'value': 3 },{'label': 'freq3', 'value': 5 },{'label': 'freq4', 'value': 7},{'label': 'freq5', 'value': 9 },
            {'label': 'acc1', 'value': 2 },{'label': 'acc2', 'value': 4 },{'label': 'acc3', 'value': 6 },{'label': 'acc4', 'value': 8 },{'label': 'acc5', 'value': 10 },
            {'label': 'RMS Acc', 'value': 11 }, {'label': 'Surface temp.', 'value': 13 }, {'label': 'RSSI', 'value': 14 }, {'label': 'Kurtosis', 'value': 12 }
        ],
        value=1
    ),
    
    dcc.Graph(id='my-graph'),

    dcc.Interval(
        id='interval-component',
        interval=3*1000,
        n_intervals=0
    )

], style={'width': '1000'})

@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value'),
    dash.dependencies.Input('interval-component', 'n_intervals')])
def update_graph(selected_dropdown_value, n):
    dfcsv=pd.read_csv('log.csv', header=None);
      
    return {
        'data': [go.Scatter(
            x=dfcsv.ix[:,0], 
            y=dfcsv.ix[:,selected_dropdown_value])
        ],
        'layout' : { 'title' : 'Node 86BD' }
    }

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
	app.run_server(host='0.0.0.0');
