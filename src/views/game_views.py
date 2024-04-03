import json

from flask import Blueprint, request, Response, make_response, render_template

from controllers.game_controller import GameController

game_views = Blueprint("game_views", __name__)

game_controller = GameController()


@game_views.route("/")
def index() -> Response:
    has_game, last_genai_response = game_controller.handle_last_game_state(
        request.cookies
    )

    response = make_response(
        render_template(
            "/pages/index.html",
            has_game=has_game,
            genai_response=last_genai_response,
        )
    )

    # response.delete_cookie("character")
    # response.delete_cookie("history")
    # response.delete_cookie("attempts")
    # response.delete_cookie("last_genai_response")

    return response


@game_views.route("/start")
def start_game() -> Response:
    response = make_response(render_template("/components/game-form.html"))

    game = game_controller.start()

    response.set_cookie("character", game.character)
    response.set_cookie("history", json.dumps(game.history))
    response.set_cookie("attempts", str(game.attempts))

    return response


@game_views.route("/ask", methods=["POST"])
def ask() -> Response:
    question = request.form["question"]
    character = request.cookies["character"]
    history = json.loads(request.cookies["history"])
    attempts = request.cookies["attempts"]

    result = game_controller.handle_question(
        question,
        {"character": character, "history": history, "attempts": attempts},
    )

    if "error" in result:
        return result["error"]

    genai_reponse = result["genai_response"]
    template = result["template"]
    game = result["game"]

    response = make_response(template)

    response.set_cookie("history", json.dumps(game.history))
    response.set_cookie("attempts", str(game.attempts))
    response.set_cookie("last_genai_response", genai_reponse)

    return response


@game_views.route("/attempts")
def get_attempts() -> Response:
    return (
        "15"
        if "attempts" not in request.cookies or request.cookies["attempts"] == "0"
        else request.cookies["attempts"]
    )


@game_views.route("/end")
def end_game() -> Response:
    attempts = request.cookies["attempts"]

    response = make_response(game_controller.handle_end_game_attempts(int(attempts)))

    response.delete_cookie("character")
    response.delete_cookie("history")
    response.delete_cookie("attempts")
    response.delete_cookie("last_genai_response")

    return response


@game_views.route("/game-button")
def get_game_button() -> str:
    return render_template("/components/game-button.html")
