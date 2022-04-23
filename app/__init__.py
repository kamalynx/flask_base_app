"""Initialize application."""
import logging
import os

from flask import Flask
from werkzeug.utils import safe_join


def create_app():
    """Create an application's instance."""
    app = Flask(__name__)

    if not os.path.exists(app.instance_path):
        os.mkdir(app.instance_path)

    if not app.debug:
        log_file = safe_join(app.instance_path, '{0}.log'.format(__name__))
        logging.basicConfig(filename=log_file, level=logging.DEBUG)

    config_file = os.path.join(app.instance_path, 'config.py')
    if os.path.exists(config_file):
        app.config.from_pyfile(config_file)

    if not app.secret_key:
        app.secret_key = os.getenv('SECRET_KEY')

    with app.app_context():
        try:
            from . import models
            from . import routes
            from . import views
        except ImportError as err:
            app.logger.warning(err)

    return app
