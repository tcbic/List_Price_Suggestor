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
    html.Div([
        html.H4("Defining the Machine Learning Problem", style={'text-decoration':'underline'}),
        html.Br(),
        html.H5("What feature in the dataset was used as the target?"),
        html.P("Price was used as the target variable."),
        html.H5("Is this a regression or classification problem?"),
        html.P('This is a regression problem given that price, a continuous number, is being predicted.'),
        html.H5("How is the target distributed?")
    ]),
        html.Div([
            html.Img(src="assets/target_distribution.PNG", width="400", height="244")]),
    html.Div([
        html.H6("Looking at the plot above, we see that the target mostly follows a normal distribution."),
        html.Br(),
        html.H5("What metric is used to evaluate the performance of the model?"),
        html.P("Mean Absolute Error is used to evaluate the model. MAE explains a model's performance in terms of how far off a prediction is on average."),
        html.H5("What are the size of the training and testing sets?"),
        html.P("Training data shape: (74, 5)"),
        html.P("Testing data shape: (25, 5)")
    ])
])

row2 = html.Div([
    html.Br(),
    html.Div([
        html.H4("Exploring the Data", style={'text-decoration':'underline', 'text-align':'center'}),
        html.Br(),
        html.H5("About the Data", style={'text-align':'center'}),
        html.P("The dataset used for modeling is data collected from the thisjourneybus eBay store. It includes sales from Summer (June) 2017 to Summer (June) 2018.", style={'text-align':'center'}),
        html.H5("Data Cleaning", style={'text-align':'center'}),
        html.P("A subset of the dataset was created to include only pre-owned Men's lululemon athletica branded items that sold under a fixed listing format.", style={'text-align':'center'}),
        html.H5("Data Engineering", style={'text-align':'center'}),
        html.P("The original dataset included a sale date feature. I chose to engineer a feature from sale date for the purpose of categorizing items based on the season in which they sold. Each item fell into one of the four seasons, Summer, Fall, Winter or Spring.", style={'text-align':'center'}),
        html.Br(),
        html.H6("The features in this table are the final features included to train the model:", style={'text-align':'center'}),
        html.Br()
    ]),
        html.Div([
            html.Img(src="assets/table.PNG", width="450", height="85")], style={'text-align':'center'}),
    html.Div([
        html.Br(),
        html.Br(),
        html.H4("Explaining Model Selection and Model Performance", style={'text-decoration':'underline'}),
        html.Br(),
        html.H5("Begin with a Baseline Model"),
        html.P("The mean of the target variable, price, is approximately $42.78."),
        html.P("Note: The primary purpose of creating a baseline is to establish a starting point to improve model performance."),
        html.P("Baseline MAE: $4.74 (If each item was listed for $42.78, it would be off by $4.74 on average.)"),
        html.H5("Model Selection"),
        html.P("To optimize model performance, I used ordinal encoding, cross-validation and randomized search (RandomizedSearchCV)."),
        html.P("Using 3-fold cross validation, the most optimal performing model is:"),
        html.H6("Random Forest Regressor with the following hyperparameters: max_depth = 10, max_features = .64621, n_estimators = 81 and random_state = 42"),
        html.P("Test MAE: $4.51 which shows an improvement of 23 cents over the baseline model.")
    ])
])

layout = dbc.Row([row1, row2])

# layout = dbc.Row([column1])