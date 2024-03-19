import json
from flask import Blueprint, request, Response, make_response, render_template
from controllers.game_controller import GameController

game_views = Blueprint("game_views", __name__)

game_controller = GameController()


@game_views.route("/")
def index() -> str:
    return render_template("/pages/index.html")


@game_views.route("/start")
def start_game() -> Response:
    response = make_response(render_template("/components/form.html"))
    response.delete_cookie("character")
    response.delete_cookie("history")
    response.delete_cookie("attempts")

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

    print(history)

    genai_reponse, game = game_controller.handle_question(
        question,
        {"character": character, "history": history, "attempts": attempts},
    )

    response = make_response(genai_reponse)

    print(genai_reponse)

    response.set_cookie("history", json.dumps(game.history))
    response.set_cookie("attempts", str(game.attempts - 1))

    return response
