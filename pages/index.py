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
            ## **Calling all Mercari sellers.**
            """,
        ), 
        dcc.Markdown(
            """
            #### Small details can mean substantial differences in sales price.
            """,
        ),
        dcc.Markdown(
            """
            #### Don't sell yourself short. Literally.
            """,
        className='mb-4'),
        dcc.Markdown(
            """
            ##### ✅ Gain insights into what sells.
            """,
        className='mb-3'),
        dcc.Markdown(
            """
            ##### ✅ Get price suggestions for how much to list an item for.
            """,
        className='mb-3'),
        dcc.Markdown(
            """
            ##### ✅ Maximize sales price and make more money.
            """,
        className='mb-4'),
        dcc.Link(dbc.Button('Get Started', color='success'), href='/predictions')
    ],
    align="center",
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])