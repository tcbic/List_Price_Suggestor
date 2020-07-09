# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """        
#             ### Insights

#             """
#         ),

#     ],
# )

row1 = html.Div([
    html.H4("Using Visualizations to Interpret Model Insights", style={'text-decoration':'underline'}),
    html.Br(),
    html.Div([
        html.H5("Permutation Importance", style={'font-style':'italic'}),
        # html.Img(src="assets/ebay_target_distribution.PNG", className="img-fluid"),
        html.P("Image, what it does and explanation specifc to model."),
        html.H5("Partial Dependence Plot", style={'font-style':'italic'}),
        # html.Img(src="assets/ebay_target_distribution.PNG", className="img-fluid"),
        html.P("Image, what it does and explanation specifc to model."),
        html.H5("Shapley Values Plot", style={'font-style':'italic'}),
        # html.Img(src="assets/ebay_target_distribution.PNG", className="img-fluid"),
        html.P("Image, what it does and explanation specifc to model.")
    ])
])

# row2 = html.Div([
#     html.Br(),
#     html.Div([
#         html.H4("Exploring the Data Cleaning Process"),
#         html.P("Details will go here."),
#         html.Br(),
#         html.H4("Explaining Model Selection and Model Performance"),
#         html.P("Details will go here.")
#     ])
# ])

layout = dbc.Row([row1])

# layout = dbc.Row([row1, row2])

# layout = dbc.Row([column1])