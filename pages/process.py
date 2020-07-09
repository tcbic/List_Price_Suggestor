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
#     [dcc.Markdown(
#             """
#             ### Process

#             """
#         ),

#     ],
# )



row1 = html.Div([
    html.H4("Defining the Machine Learning Problem"),
    html.Br(),
    html.Div([
        html.H5("What feature in the dataset was used as the target?", style={'font-style':'italic'}),
        html.P("Price was used as the target variable."),
        html.H5("Is this a regression or classification problem?", style={'font-style':'italic'}),
        html.P("This is a regression problem given that price, a continuous  is being predicted."),
        html.H5("How is the target distributed?", style={'font-style':'italic'}),
        html.Img(src="assets/ebay_target_distribution.PNG", className="img-fluid"),
        html.H5("What metric is used to evaluate the performance of the model?", style={'font-style':'italic'}),
        html.P("Mean Absolute Error is used to evaluate the model. MAE explains a model's performance in terms of answering how far off a prediction is on average."),
        html.H5("What is the size of the train and test set?", style={'font-style':'italic'}),
        html.P("Training data shape: (74, 5)"),
        html.P("Testing data shape: (25, 5)")
    ])
])

row2 = html.Div([
    html.Br(),
    html.Div([
        html.H4("Exploring the Data Cleaning Process"),
        html.P("Details will go here."),
        html.Br(),
        html.H4("Explaining Model Selection and Model Performance"),
        html.P("Details will go here.")
    ])
])


layout = dbc.Row([row1, row2])

# layout = dbc.Row([column1])