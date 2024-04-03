from flask import Flask

from .error_views import error_views
from .game_views import game_views


def init_views(app: Flask) -> None:
    app.register_blueprint(error_views)
    app.register_blueprint(game_views)
