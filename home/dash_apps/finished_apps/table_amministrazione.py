import dash
import dash_table
import pandas as pd
from django_plotly_dash import DjangoDash
from .nutrienti import cibo_mangiato, identifica
import datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django.contrib.auth.models import User
import numpy as np

import pymongo
from pymongo import MongoClient
import ssl
import datetime

# Sistemare tutto
client = pymongo.MongoClient("mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
#db = client.test
db = client['ArmoniaBot']
col = db['AlimentiDB']
prove = col.find({},{'Nome':1})
nomi =[]
for pro in prove:
    nomi.append(pro['Nome'])
    #data['Nome'].append(pro['Nome'])
#df = cibo_mangiato('Pranzo','AlessioNone',datetime.datetime(2021,7,15))
#print(df)
df = pd.DataFrame()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Cibo2', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.P(html.Strong('Colazione')),
    dash_table.DataTable(
    id='table-colazione',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True,
style_as_list_view=True,
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
    ),
    # dcc.DatePickerSingle(
    #     id='my-date-picker-single1',
    #     min_date_allowed=datetime.datetime(2020, 1, 1),
    #     max_date_allowed=datetime.datetime(2026, 1, 1),
    #     initial_visible_month=datetime.datetime(2017, 8, 5),
    #     date=datetime.date.today()#datetime(2017, 8, 25)
    # ),
html.P(html.Strong('Pranzo')),
dash_table.DataTable(
    id='table-pranzo',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True,
    ),
    # dcc.DatePickerSingle(
    #     id='my-date-picker-single2',
    #     min_date_allowed=datetime.datetime(2020, 1, 1),
    #     max_date_allowed=datetime.datetime(2026, 1, 1),
    #     initial_visible_month=datetime.datetime(2017, 8, 5),
    #     date=datetime.date.today()#datetime(2017, 8, 25)
    # ),
html.P(html.Strong('Cena')),
dash_table.DataTable(
    id='table-cena',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True
    ),
    # dcc.DatePickerSingle(
    #     id='my-date-picker-single3',
    #     min_date_allowed=datetime.datetime(2020, 1, 1),
    #     max_date_allowed=datetime.datetime(2026, 1, 1),
    #     initial_visible_month=datetime.datetime(2017, 8, 5),
    #     date=datetime.date.today()#datetime(2017, 8, 25)
    # ),
html.P(html.Strong('Merenda')),
dash_table.DataTable(
    id='table-merenda',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True
    ),
html.P(html.Strong('Seleziona la data:')),
    dcc.DatePickerSingle(
        id='my-date-picker-single4',
        min_date_allowed=datetime.datetime(2020, 1, 1),
        max_date_allowed=datetime.datetime(2026, 1, 1),
        initial_visible_month=datetime.datetime(2017, 8, 5),
        date=datetime.date.today()#datetime(2017, 8, 25)
    ),
html.P(html.Strong('Utenti')),
    dcc.Dropdown(
        id='slider-radio-user',
        options=[
            {"label": user, "value": user}
            for user in np.sort(np.unique(nomi))#data.Nome.unique())
        ],
        value='AlessioNone'
    ),
])

@app.callback(
               Output('table-colazione', 'data'),
               Output('table-colazione', 'columns'),
              [Input('my-date-picker-single4', 'date'),
               Input('slider-radio-user', 'value'),])
def display_value(value, user):
    print(value)
    dt =datetime.datetime.strptime(value, '%Y-%m-%d')
    #dt = datetime.datetime.combine(value, datetime.datetime.min.time())
    print(dt)
    df = cibo_mangiato('Colazione', user, dt)
    print(df)
    return [df.to_dict('records'),[{"name": i, "id": i} for i in df.columns]]
    #raise PreventUpdate
@app.callback(
               Output('table-pranzo', 'data'),
               Output('table-pranzo', 'columns'),
              [Input('my-date-picker-single4', 'date'),
               Input('slider-radio-user', 'value'),])
def display_value(value,user):
    print(value)
    dt =datetime.datetime.strptime(value, '%Y-%m-%d')
    #dt = datetime.datetime.combine(value, datetime.datetime.min.time())
    print(dt)
    df = cibo_mangiato('Pranzo', user, dt)
    print(df)
    return [df.to_dict('records'),[{"name": i, "id": i} for i in df.columns]]

@app.callback(
               Output('table-cena', 'data'),
               Output('table-cena', 'columns'),
              [Input('my-date-picker-single4', 'date'),
               Input('slider-radio-user', 'value'),])
def display_value(value,user):
    print(value)
    dt =datetime.datetime.strptime(value, '%Y-%m-%d')
    #dt = datetime.datetime.combine(value, datetime.datetime.min.time())
    print(dt)
    df = cibo_mangiato('Cena', user, dt)
    print(df)
    return [df.to_dict('records'),[{"name": i, "id": i} for i in df.columns]]

@app.callback(
               Output('table-merenda', 'data'),
               Output('table-merenda', 'columns'),
              [Input('my-date-picker-single4', 'date'),
               Input('slider-radio-user', 'value'),])
def display_value(value,user):
    print(value)
    dt =datetime.datetime.strptime(value, '%Y-%m-%d')
    #dt = datetime.datetime.combine(value, datetime.datetime.min.time())
    print(dt)
    df = cibo_mangiato('Merenda', user, dt)
    print(df)
    return [df.to_dict('records'),[{"name": i, "id": i} for i in df.columns]]


if __name__ == '__main__':
    app.run_server(debug=True)