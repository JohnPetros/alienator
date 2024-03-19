from flask import Flask
from views import init_views


def create_app() -> Flask:
    app = Flask(__name__, template_folder="./ui/templates", static_folder="./ui/static")

    init_views(app)

    return app
