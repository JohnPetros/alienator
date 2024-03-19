from flask import Blueprint, render_template

error_views = Blueprint("error_views", __name__)


@error_views.errorhandler(500)
def handle_500_error(error) -> str:
    print("error", error)
    return render_template("/components/error-button.html")


@error_views.errorhandler(400)
def handle_400_error(error) -> str:
    print("error", error)
    return render_template("/components/error-button.html")
