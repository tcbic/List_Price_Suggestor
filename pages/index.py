# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(className='mb-5'),
        dcc.Markdown(
            """
            ### **It's often not easy to gauge how much an item is worth, and list price can be the difference as to whether an item sells or not.**
            """, style={'text-align':'center'}
        ), 
        html.Br(),
        # dcc.Markdown(
        #     """
        #     ##### This makes recommendation tools a helpful guide.
        #     """, style={'text-align':'center'}
        # ),
        # dcc.Markdown(
        #     """
        #     ##### Selling online is becoming more and more common practice.
        #     """,
        # className='mb-3'),
        dcc.Markdown(
            """
            ##### lululemon athletica has been one of the top selling brands on the thisjourneybus eBay store. To the right, you see the most popular lululemon Men's styles sold.
            """, style={'text-align':'center'},
        className='mb-3'),
        dcc.Markdown(
            """
            ##### Interested and ready to sell Men's lululemon athletica on eBay?
            """, style={'text-align':'center'},
        className='mb-4'),
        html.Br(),
        dcc.Link(dbc.Button('Get Started Here', color='primary'), href='/predictions')
    ], style={'text-align':'center'},
    width=6,
)

column2 = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Img(src="assets/mens_top_styles.PNG", width="565", height="266")])    

layout = dbc.Row([column1, column2])