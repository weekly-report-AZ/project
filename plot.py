import dash
import pandas as pd
from datetime import datetime
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html


class Plot:
    def __init__(self):
        self.ga_data = pd.read_csv("report_g.csv", sep=';')
        self.ym_data = pd.read_csv("report_y.csv", sep=';')

        self.sites = list(self.ga_data.columns)
        self.sites.remove('date')

        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

        self.app = dash.Dash(__name__,
                             external_stylesheets=external_stylesheets)

        self.app.layout = html.Div(
            [
                dcc.Dropdown(
                    id='my-dropdown',
                    options=[
                        {
                            'label': i,
                            'value': i
                        }
                        for i in self.sites],
                    value=self.sites,
                    multi=True
                ),
                dcc.Graph(
                    id='ga-graph',
                    figure=go.Figure(
                        data=[
                            go.Scatter(
                                x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                                   for d in self.ga_data.date],
                                y=self.ga_data[v],
                                name=v
                            ) for v in self.sites
                        ],
                        layout=go.Layout(
                            title='Google analytics',
                            showlegend=True,
                            legend=go.layout.Legend(x=0, y=1.0),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 340},
                ),
                dcc.Graph(
                    id='ym-graph',
                    figure=go.Figure(
                        data=[
                            go.Scatter(
                                x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                                   for d in self.ym_data.date],
                                y=self.ym_data[v],
                                name=v
                            ) for v in self.sites
                        ],
                        layout=go.Layout(
                            title='Yandex metrika',
                            showlegend=True,
                            legend=go.layout.Legend(x=0, y=1.0),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 340},
                ),
                html.Div([html.Button('Update', id='button')]),
                html.Div(id='output-container')
            ]
        )

        @self.app.callback(
            dash.dependencies.Output('ga-graph', 'figure'),
            [dash.dependencies.Input('my-dropdown', 'value')])
        def update_figure(value):
            if value:
                data = [
                   go.Scatter(
                       x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                          for d in self.ga_data.date],
                       y=self.ga_data[v],
                       name=v
                    ) for v in value
                ]
            else:
                data = [
                    go.Scatter(
                        x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                           for d in self.ga_data.date],
                        y=[]
                    )
                ]

            layout = go.Layout(
                title='Google analytics',
                showlegend=True,
                legend=go.layout.Legend(x=0, y=1.0),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )

            return {'data': data, 'layout': layout}

        @self.app.callback(
            dash.dependencies.Output('ym-graph', 'figure'),
            [dash.dependencies.Input('my-dropdown', 'value')])
        def update_figure(value):
            if value:
                data = [
                    go.Scatter(
                        x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                           for d in self.ym_data.date],
                        y=self.ym_data[v],
                        name=v
                    ) for v in value
                ]
            else:
                data = [
                    go.Scatter(
                        x=[datetime.strptime(d, '%d.%m.%Y %H:%M')
                           for d in self.ym_data.date],
                        y=[]
                    )
                ]

            layout = go.Layout(
                title='Yandex metrika',
                showlegend=True,
                legend=go.layout.Legend(x=0, y=1.0),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )

            return {'data': data, 'layout': layout}

        @self.app.callback(
            dash.dependencies.Output('my-dropdown', 'options'),
            [dash.dependencies.Input('my-dropdown', 'value')])
        def set_b_options(a_val):
            return [{'value': i, 'label': i} for i in a_val]

        @self.app.callback(
            dash.dependencies.Output('my-dropdown', 'value'),
            [dash.dependencies.Input('button', 'n_clicks')])
        def update_a_to_default(clicks):
            self.ga_data = pd.read_csv("report_g.csv", sep=';')
            self.ym_data = pd.read_csv("report_y.csv", sep=';')

            self.sites = list(self.ga_data.columns)
            self.sites.remove('date')
            return self.sites


if __name__ == '__main__':
    plot = Plot()
    plot.app.run_server(debug=True)