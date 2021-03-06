# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
import numpy as np

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Br(),
        dcc.Markdown(
            """
        
            #### Select the features below based on the item intended for listing.
            ###### Note: All suggestions assume an item is pre-owned and in excellent selling condition (i.e. No tears, holes, stains or pilling.).

            """, style={'text-align':'center'},
        className='mb-4'),
        dcc.Markdown('##### ** Size **'),
        dcc.RadioItems(
            id = 'size',
            options = [
                {'label': 'S', 'value': 4},
                {'label': 'M', 'value': 1},
                {'label': 'L', 'value': 2},
                {'label': 'XL', 'value': 3},
                {'label': 'XXL', 'value': 5}
            ],
            value=1,
            labelStyle = {'margin-right': '25px'},
            className='mb-3',
        ),        
        dcc.Markdown('##### ** Style **'),
        dcc.Dropdown(
            id = 'style',
            options = [
                {'label': 'Metal Vent Tech Shirt', 'value': 2},
                {'label': 'Metal Vent Tech Polo', 'value': 7},
                {'label': 'Metal Vent Tech Tank Top', 'value': 6},
                {'label': 'Metal Vent Tech 1/2 Zip', 'value': 5},
                {'label': 'T.H.E. Short', 'value': 3},
                {'label': 'Surge Short', 'value': 4},
                {'label': 'Pace Breaker Short', 'value': 1}
            ],
            value=4,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Item Specifics **'),
        dcc.Dropdown(
            id = 'item-specifics',
            options = [
                {'label': 'Linerless', 'value': 1},
                {'label': 'Lined', 'value': 4},
                {'label': 'Long Sleeve', 'value': 3},
                {'label': 'Short Sleeve', 'value': 2},
                {'label': 'Sleeveless', 'value': 5}
            ],
            value=4,
            className='mb-3',
        ),
        dcc.Markdown('##### ** Current Selling Season **'),
        dcc.RadioItems(
            id = 'season',
            options = [
                {'label': 'Summer', 'value': 4},
                {'label': 'Fall', 'value': 2},
                {'label': 'Winter', 'value': 1},
                {'label': 'Spring', 'value': 3}
            ],
            value=1,
            labelStyle = {'margin-right': '25px'},
            className='mb-3',
        ),
        dcc.Markdown('##### ** The suggested list price is: **', className='mb-2', style={'text-align':'center'}), html.Div( id='prediction-content', style={'text-align':'center'})
    ],
)

# column2 = dbc.Col(
#     [

#     ]
# )

layout = dbc.Row([column1])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('size', 'value'), 
    Input('style', 'value'),
    Input('item-specifics', 'value'),
    Input('season', 'value')])

def predict(size, style, item_specifics, season):
    df = pd.DataFrame(
        columns=['size', 'style', 'item_specifics', 'season'],
        data=[[size, style, item_specifics, season]]
    )

    pipeline = load('assets/pipeline_b.joblib')
    y_pred = pipeline.predict(df)[0]
    # y_pred_log = pipeline.predict(df)
    # y_pred = np.expm1(y_pred_log)[0]
    return f'${y_pred:.2f} dollars'