"""Define application's routes."""
from flask import current_app

from . import views


current_app.add_url_rule('/', view_func=views.index)