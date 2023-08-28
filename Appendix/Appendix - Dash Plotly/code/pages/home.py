import dash
from dash import Dash, html, callback, Output, Input, State, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__, path='/')

layout =  dbc.Container([
    html.H1("Welcome the student of ML2023."),
    html.H1("I hope you are enjoying coding!!!"),

], fluid=True)