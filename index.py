from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import dash

from app import *
from pages import login, register, data

#from dash_bootstrap_templates import load_figure_template
#load_figure_template(["quartz"])


# ===== Layout ====
app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="base-url", refresh=False),
            html.Div(id="page-content", style={"height": "100vh", "display":"flex", "justify-content": "center"})

        ]),
    ])
],fluid = True)

@app.callback(Output("page-content","children"),
              Input("base-url","pathname"),
              )

def render_page_content(pathname):
    if (pathname == "/login" or pathname == "/"):
        return login.render_layout()
    if pathname == "/register":
        return register.render_layout()
    if pathname == "/data":
        return data.render_layout("Luzo")


if __name__ == "__main__":
    app.run_server(port = 8051, debug=True)