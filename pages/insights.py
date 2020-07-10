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
        html.H4("Permutation Importance", style={'font-style':'italic', 'text-align':'center'}),
        html.P("Permutation importance is one way of measuring what features have the biggest impact on model predictions.", style={'text-align':'center'}),
        html.P("The values toward the top are the most important features while the features toward the bottom matter least. The first number indicates how much model performance decreased with a random shuffling, and the second number measures how much performance varied from one-reshuffling to the next.", style={'text-align':'center'}),
        html.P("Looking at the permutation importance below, we see that the two most important features are style and item specifics.", style={'text-align':'center'})
    ]),
        html.Div([
            html.Img(src="assets/lulu_permutation_importance.PNG")], style={'text-align':'center'}),
        html.Div([
        html.Br(),
        html.H4("Partial Dependence Plots", style={'font-style':'italic', 'text-align':'center'}),
        html.P("A partial dependence plot can show how a variable affects a model's predictions.", style={'text-align':'center'}),
        html.P("We'll see how the model output across different lululemon athletica Men's styles and item specifics affect suggested price.", style={'text-align':'center'}),
        html.Br(),
        html.H6("Partial Dependence Plot (Style)", style={'text-decoration':'underline', 'text-align':'center'})
        ]),
            html.Div([
                html.Img(src="assets/partial_dependence.PNG", width="700", height="454")], style={'text-align':'center'}),
            html.Div([
                html.Br(),
                html.H6("Notice that the Metal Vent Tech 1/2 Zip style affects the suggested list price the most. It has an increased impact on price.", style={'text-align':'center'})
            ]),
                html.Br(),
                html.Br(),
                html.Div([
                    html.H6("Partial Dependence Plot (Item Specifics)", style={'text-decoration':'underline', 'text-align':'center'})
                ]),
                    html.Div([
                        html.Img(src="assets/partial_dependence_2.PNG", width="700", height="454")], style={'text-align':'center'}),
                    html.Div([
                        html.Br(),
                        html.H6("A long sleeve item has the highest positive impact on price and a sleeveless item has the largest negative impact on price.", style={'text-align':'center'})
                    ]),
                        html.Br(),
                        html.Br(),
                        html.Div([
                            html.H4("Shapley Values Plot", style={'font-style':'italic', 'text-align':'center'}),
                            html.P("SHAP values break down one prediction to show the impact of each feature.", style={'text-align':'center'}),
                            html.P("To demonstrate, let's take a closer look at an observation from the testing set.", style={'text-align':'center'}),
                            html.P("This observation has the following values for each feature: size - L, style - Surge Short, item_specifics - Linerless, season - Spring", style={'text-align':'center'}),
                            html.P("We know that this item was listed and sold for $44.99.", style={'text-align':'center'}),
                            html.Br(),
                            html.H6("What did the selected model predict to list this item at?", style={'text-align':'center'}),
                            html.P("Below within the Shapley Value plot, we see that the model suggested to list this item at $41.55.", style={'text-align':'center'})
                        ]),
                            html.Div([
                                html.Img(src="assets/lulu_shapley_value.PNG", width="900", height="144")], style={'text-align':'center'}),
                            html.Div([
                                html.Br(),
                                html.H6("How much does each feature affect the suggested listing price for this item?"),
                                html.Br(),
                                html.Img(src="assets/shapley_details.PNG", width="275", height="83")], style={'text-align':'center'}),
                            html.Div([
                                html.Br(),
                                html.P("By looking at the above values, we see that this item's style, item specifics and season contributed negatively to the suggested listing price.", style={'text-align':'center'}),
                                html.P("Size was the only feature that contributed to increasing price.", style={'text-align':'center'})
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