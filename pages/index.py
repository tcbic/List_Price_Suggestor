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
            ## **The specifc styles within a given brand mean something.**
            """,
        ), 
        dcc.Markdown(
            """
            #### Not just in terms of looks, but also sales price.
            """,
        ),
        dcc.Markdown(
            """
            ##### lululemon athletica has become a mainstream athletic apparel brand.
            """,
        className='mb-3'),
        dcc.Markdown(
            """
            ##### This app aims to offer list price suggestions for some of their most popular men's styles.
            """,
        className='mb-3'),
        dcc.Markdown(
            """
            ##### All list price suggestions assume that the item is in excellent pre-owned condition and will be sold on eBay.
            """,
        className='mb-4'),
        dcc.Link(dbc.Button('Get Started Here', color='success'), href='/predictions')
    ],
    align="center",
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )

layout = dbc.Row([column1])
# layout = dbc.Row([column1, column2])