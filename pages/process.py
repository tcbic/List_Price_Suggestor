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
    html.H4("Defining the Machine Learning Problem", style={'text-decoration':'underline'}),
    html.Br(),
    html.Div([
        html.H5("What feature in the dataset was used as the target?", style={'font-style':'italic', 'text-align':'center'}),
        html.P("Price was used as the target variable.", style={'text-align':'center'}),
        html.H5("Is this a regression or classification problem?", style={'font-style':'italic', 'text-align':'center'}),
        html.P('This is a regression problem given that price, a continuous number, is being predicted. In a regression problem, we are most often predicting "How much/How many?"', style={'text-align':'center'}),
        html.H5("How is the target distributed?", style={'font-style':'italic', 'text-align':'center'})
    ]),
        html.Div([
            html.Img(src="assets/target_distribution.PNG", width="400", height="244")], style={'text-align':'center'}),
        html.Div([
        html.P("Looking at the plot above, we see that the target mostly follows a normal distribution.", style={'text-align':'center'}),
        html.H5("What metric is used to evaluate the performance of the model?", style={'font-style':'italic', 'text-align':'center'}),
        html.P("Mean Absolute Error is used to evaluate the model. MAE explains a model's performance in terms of how far off a prediction is on average.", style={'text-align':'center'}),
        html.H5("What are the sizes of the training and testing sets?", style={'font-style':'italic', 'text-align':'center'}),
        html.P("Training data shape: (74, 5)", style={'text-align':'center'}),
        html.P("Testing data shape: (25, 5)", style={'text-align':'center'})
    ])
])

row2 = html.Div([
    html.Br(),
    html.Div([
        html.H4("Exploring the Data", style={'text-decoration':'underline'}),
        html.Br(),
        html.H5("About the Data", style={'font-style':'italic', 'text-align':'center'}),
        html.P('The dataset used for modeling is data collected from "thisjourneybus" eBay store. It includes sales from Summer (June) 2017 to Summer (June) 2018.', style={'text-align':'center'}),
        html.H5("Data Cleaning", style={'font-style':'italic', 'text-align':'center'}),
        html.P("A subset of the dataset was created to include only Men's lululemon athletica branded items that sold as a fixed listing format.", style={'text-align':'center'}),
        html.H5("Data Engineering", style={'font-style':'italic', 'text-align':'center'}),
        html.P("I chose to engineer a feature from sale date for the purpose of categorizing items based on the season in which they sold. Each item fell into one of the four seasons, Summer, Fall, Winter or Spring.", style={'text-align':'center'}),
        html.H6("The final features included in the dataset used to train the model are:", style={'text-align':'center'}),
        html.P("size - the size of the item sold", style={'font-style':'italic', 'text-align':'center'}),
        html.P("style - the name of the specific lululemon athletica style", style={'font-style':'italic', 'text-align':'center'}),
        html.P("item_specifcs - a descriptor of the item sold", style={'font-style':'italic', 'text-align':'center'}),
        html.P("season - the season the item sold (i.e. Fall)", style={'font-style':'italic', 'text-align':'center'}),
        html.Br(),
        html.H4("Explaining Model Selection and Model Performance", style={'text-decoration':'underline'}),
        html.Br(),
        html.H5("Begin with a Baseline Model", style={'font-style':'italic', 'text-align':'center'}),
        html.P("The mean of the target variable, price, is approximately $42.78. I used the mean to create a baseline model. The primary purpose of creating a baseline is to establish a starting point to improve upon.", style={'text-align':'center'}),
        html.P("If each item was listed for $42.78, it would be off by $4.74 on average.", style={'text-align':'center'}),
        html.H5("Model Selection", style={'font-style':'italic', 'text-align':'center'}),
        html.P("To optimize model performance, I used ordinal encoding, cross-validation and randomized search (RandomizedSearchCV).", style={'text-align':'center'}),
        html.P("Using 3-fold cross validation, the most optimal performing model is:", style={'text-align':'center'}),
        html.H6("Random Forest Regressor with the following hyperparameters: max_depth = 10, max_features = .64621, n_estimators = 81 and random_state = 42", style={'text-align':'center'}),
        html.P("This model has a test MAE of $4.51 and shows an improvement of 23 cents over the baseline model.", style={'text-align':'center'}),
        html.P("Note: A random forest model is an example of a tree model; more specifically, a tree ensemble model.", style={'text-align':'center'})

    ])
])


layout = dbc.Row([row1, row2])

# layout = dbc.Row([column1])