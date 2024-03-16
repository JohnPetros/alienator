from flask import Flask
import views


def create_app():
    app = Flask(__name__)

    views.init(app)

    return app
