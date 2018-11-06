import dash
<<<<<<< HEAD
import xlrd
from datetime import datetime
import plotly.graph_objs as go
=======
import pandas as pd
>>>>>>> 169af6e5dfcfb0dcf1b766ede2e9fc16db89eb30
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime
import plotly.graph_objs as go



class Plot:
    def __init__(self):
        self.work_book = xlrd.open_workbook("report.xlsx")
        self.yandex_sheet = self.work_book.sheet_by_name('Yandex')
        self.google_sheet = self.work_book.sheet_by_name('Google')

        self.sites = [e.value for e in self.yandex_sheet.row(0)]
        self.sites.remove('date')

        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

        self.app = dash.Dash(__name__,
                             external_stylesheets=external_stylesheets)

        gx_axis = [datetime.strptime(self.google_sheet.row(v)[0].value, '%d.%m.%Y %H:%M')
                   for v in range(1, self.google_sheet.nrows)]

        yx_axis = [datetime.strptime(self.yandex_sheet.row(v)[0].value, '%d.%m.%Y %H:%M')
                   for v in range(1, self.yandex_sheet.nrows)]

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
                                x=gx_axis,
                                y=[int(f) for f in self.google_sheet.col_values(self.sites.index(v) + 1)[1:]],
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
                                x=yx_axis,
                                y=[int(f) for f in self.yandex_sheet.col_values(
                                    self.sites.index(v) + 1)[1:]],
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
                       x=yx_axis,
                       y=[int(f) for f in self.google_sheet.col_values(
                                    self.sites.index(v) + 1)[1:]],
                       name=v
                    ) for v in value
                ]
            else:
                data = [
                    go.Scatter(
                        x=gx_axis,
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
                        x=yx_axis,
                        y=[int(f) for f in self.yandex_sheet.col_values(
                                    self.sites.index(v) + 1)[1:]],
                        name=v
                    ) for v in value
                ]
            else:
                data = [
                    go.Scatter(
                        x=yx_axis,
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
            self.work_book = xlrd.open_workbook("report.xlsx")

            self.sites = [e.value for e in self.yandex_sheet.row(0)]
            self.sites.remove('date')
            return self.sites


if __name__ == '__main__':
    plot = Plot()
    plot.app.run_server(debug=True)