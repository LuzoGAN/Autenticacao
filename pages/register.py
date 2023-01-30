from dash import html,dcc
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import plotly.express as px

card_style = {
    "widht" : "300px",
    "min-height": "300px",
    "padding-top": "25px",
    "padding-right": "25px",
    "padding-left": "25px",
    "align-self": "center"
}

def render_layout():
    register = dbc.Card([
        html.Legend("Registrar"),
        dbc.Input(id="user_register", placeholder="Username", type="text"),
        dbc.Input(id="pwd_register", placeholder="Password", type="password"),
        dbc.Button("register", id="register_button"),
        html.Span("",style={"text-align": "center"}),
        html.Div([
            html.Label("Ou",style={"margin=right": "5px"}),
            dcc.Link("faça login", href="register")
        ], style={"padding": "20px","justify-content": "center", "display": "flex"})

    ],style = card_style)
    return register