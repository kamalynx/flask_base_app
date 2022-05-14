"""Define your views here."""
from datetime import datetime


def index():
    """Return current date for example."""
    now = datetime.now().strftime('%d %B %Y')
    return f'Hello from flask base app. Today is {now}'
