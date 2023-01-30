import dash
import dash_bootstrap_components as dbc

from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import configparser
import os

#from dash_bootstrap_templates import load_figure_template
#load_figure_template(["quartz"])

app = dash.Dash(__name__)#, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server