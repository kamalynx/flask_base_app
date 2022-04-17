"""Define application's routes."""
from flask import current_app as app

from . import views


app.add_url_rule('/', view_func=views.index)
