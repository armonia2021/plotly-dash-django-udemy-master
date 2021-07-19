import dash_core_components as dcc
#import dash_design_kit as ddk
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from .nutrienti import grafico,calcola_nutrienti,dataframe_nutrimenti
import pandas as pd
import numpy as np
from django.contrib.auth.models import User


#xc,yc, xa,ya = grafico()
import pymongo
from pymongo import MongoClient
import ssl
import datetime

# Sistemare tutto
client = pymongo.MongoClient("mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
#db = client.test
db = client['ArmoniaBot']
col = db['AlimentiDB']

prove = col.find()#{'Nome':'AlessioNone'})
data = pd.DataFrame()
for prova in prove:
    date = prova['Data']
    colazione = calcola_nutrienti(prova,'Colazione')
    pranzo = calcola_nutrienti(prova,'Pranzo')
    cena = calcola_nutrienti(prova,'Cena')
    merenda = calcola_nutrienti(prova,'Merenda')
    dff,cola,pra,cen,mere = dataframe_nutrimenti(colazione, pranzo,cena,merenda,date)
    dff['Nome'] = prova['Nome']
    data = data.append(dff)
data['Data'] = data.index
data["Data"] = pd.to_datetime(data["Data"], format="%Y-%m-%d")
data.sort_values("Data", inplace=True)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Armonia', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1('Andamento nutrienti'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    html.P(html.Strong('Nutrienti')),
    dcc.RadioItems(
        id='slider-radio',
        options=[
            {'label': 'Calorie', 'value': 'cal'},
            {'label': 'Acqua', 'value': 'acq'},
        ],
        value='cal',
        labelStyle={'display': 'inline-block'},
    ),
    html.P(html.Strong('Utenti')),
    dcc.Dropdown(
        id='slider-radio-user',
        options=[
            {"label": user, "value": user}
            for user in np.sort(data.Nome.unique())
        ],
        value='AlessioNone'
    ),
#     dcc.RadioItems(
#        id='slider-radio-user',
#        options=[
#            {"label": user, "value": user}
#            for user in np.sort(data.Nome.unique())
#
#        ],
#        value='AlessioNone',
#        labelStyle={'display': 'inline-block'}
#    )

])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-radio', 'value'),
               Input('slider-radio-user', 'value')])
def display_value(value,user):
    from .nutrienti import grafico

    mask = (
            (data.Nome == user)
    )
    filtered_data = data.loc[mask, :]
    if value=='cal':
        #x,y = grafico('Calorie')
        #x=xc
        #y=yc
        x=filtered_data['Data']
        y=filtered_data['Calorie']
        suff = ' kcal'
    elif value=='acq':
        #x,y = grafico('Acqua')
        #x=xa
        #y=ya
        x = filtered_data['Data']
        y = filtered_data['Acqua']
        suff = ' ml'

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
        #name = username
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(ticksuffix=suff, range=[min(y), max(y)]),
        #xaxis=dict(range=[min(x), max(x)]),
        #yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),
        #showlegend=True,

    )
    return {'data': [graph], 'layout': layout}
