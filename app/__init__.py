"""Initialize application."""
from flask import Flask


def create_app():
    """Create an application's instance."""
    app = Flask(__name__)

    with app.app_context():
        try:
            from . import models
            from . import routes
            from . import views
        except ImportError as err:
            app.logger.warning(err)

    return app
