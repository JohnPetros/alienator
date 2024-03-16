from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def page():
    return render_template("/pages/index.html")


def init(app):
    app.register_blueprint(views)
