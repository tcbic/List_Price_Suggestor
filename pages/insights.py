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
        html.H5("Permutation Importance", style={'font-style':'italic', 'text-align':'center'}),
        html.P("Permutation importance is one way of measuring what features have the biggest impact on model predictions. It's calculated after a model has been fitted.", style={'text-align':'center'}),
        html.P("The values toward the top are the most important features while the features toward the bottom matter least. The first number indicates how much model performance decreased with a random shuffling, and the second number measures how much performance varied from one-reshuffling to the next.", style={'text-align':'center'}),
        html.P("Looking at the permutation importance, we see that the two most important features are style and item specifics.", style={'text-align':'center'})
    ]),
        html.Div([
            html.Img(src="assets/lulu_permutation_importance.PNG")], style={'text-align':'center'}),
        html.Div([
        html.H5("Partial Dependence Plots", style={'font-style':'italic', 'text-align':'center'}),
        html.P("A partial dependence plot shows how a variable affects a model's predictions. Just like permutation importance, partial dependence is calculated after a model has been fit.", style={'text-align':'center'}),
        html.P("Below see what happens to the model output across different lululemon athletica Men's styles and different item specifics.", style={'text-align':'center'}),
        html.H6("Partial Dependence Plot (Style)", style={'text-align':'center'})
        ]),
            html.Div([
                html.Img(src="assets/partial_dependence.PNG", width="700", height="454")], style={'text-align':'center'}),
            html.Br(),
            html.Br(),
            html.Div([
                html.H6("Partial Dependence Plot (Item Specifics)", style={'text-align':'center'})
            ]),
                html.Div([
                    html.Img(src="assets/partial_dependence_2.PNG", width="700", height="454")], style={'text-align':'center'}),
                html.Br(),
                html.Br(),
                html.Div([
                    html.H5("Shapley Values Plots", style={'font-style':'italic', 'text-align':'center'})
                ]),
                    html.Div([
                        # html.Img(src="assets/ebay_target_distribution.PNG", className="img-fluid"),
                        html.P("Image, what it does and explanation specifc to model.", style={'text-align':'center'})
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