import dash
from dash import Dash, html, callback, Output, Input, State, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__, path='/model1')


# Creating FORM
x_1 = html.Div(
    [
        dbc.Label("x_1", html_for="example-email"),
        dbc.Input(id="x_1", type="number", placeholder="Put a value for x_1"),
        dbc.FormText(
            "This is the value for x_1",
            color="secondary",
        ),
    ],
    className="mb-3",
)

x_2 = html.Div(
    [
        dbc.Label("x_2", html_for="example-email"),
        dbc.Input(id="x_2", type="number", placeholder="Put a value for x_2"),
        dbc.FormText(
            "This is the value for x_2",
            color="secondary",
        ),
    ],
    className="mb-3",
)

submit_hardcode = html.Div([
            dbc.Button(id="submit_hardcode", children="calculate y using hardcode", color="primary", className="me-1"),
            dbc.Label("y is: "),
            html.Output(id="y_hardcode", children="")
], style={'marginTop':'10px'})

submit_model = html.Div([
            dbc.Button(id="submit_model", children="calculate y using model", color="primary", className="me-1"),
            dbc.Label("y is: "),
            html.Output(id="y_model", children="")
], style={'marginTop':'10px'})

form =  dbc.Form([
            x_1,
            x_2,
            submit_hardcode,
            submit_model
        ],
        className="mb-3")


# Explain Text
text = html.Div([
    html.H1("The first Assigment sample"),
    html.P("I have two models to show. The goal is to predict y when the relation of y is y = x_1 + x_2."),
    html.P("The first model is basically a hardcoded y = x_1 + x_2. Very simple."),
    html.P("The second model is create a dataset and train a LinearRegrssion model. Then, use that model to predict y using an input x_1, x_2. The coef of the model is [1,1] shows that the model can learn this relation perfectly."),
])

# Dataset Example
from dash import Dash, dash_table
import pandas as pd
df = pd.read_csv('./dataset/dataset.csv')

table = dbc.Table.from_dataframe(df, 
                        striped=True, 
                        bordered=True, 
                        hover=True,
                        responsive=True,
                        size='sm'
                            )

layout =  dbc.Container([
        text,
        form,
        html.H1("The Dataset I use to train the model"),
        table
    ], fluid=True)

@callback(
    Output(component_id="y_hardcode", component_property="children"),
    State(component_id="x_1", component_property="value"),
    State(component_id="x_2", component_property="value"),
    Input(component_id="submit_hardcode", component_property='n_clicks'),
    prevent_initial_call=True
)
def calculate_y_hardcode(x_1, x_2, submit):
    print(x_1)
    print(x_2)
    print(submit)
    return x_1 + x_2

@callback(
    Output(component_id="y_model", component_property="children"),
    State(component_id="x_1", component_property="value"),
    State(component_id="x_2", component_property="value"),
    Input(component_id="submit_model", component_property='n_clicks'),
    prevent_initial_call=True
)
def calculate_y_model(x_1, x_2, submit):
    pred = calculate_model(x_1,x_2)
    coef = get_coeff()
    return f" model said: {pred=} {coef_=}"

def get_coeff():
    from utils import load
    model = load('./models/myModel.pickle')
    return model.coef_

def calculate_model(x_1,x_2):
    from utils import load
    import pandas as pd
    import numpy as np
    model = load('./models/myModel.pickle')
    X = np.array([x_1,x_2]).reshape(-1,2)
    X = pd.DataFrame(X, columns=['x1', 'x2']) 
    pred = model.predict(X)
    return pred