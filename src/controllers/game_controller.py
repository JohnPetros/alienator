from typing import Dict, Tuple

from providers.genai_provider import GenAiProvider
from models.game_model import GameModel
from utils.app_error import AppError

genai = GenAiProvider()


class GameController:
    def start(self) -> GameModel:
        initial_prompt = "Let's play a game where you think of a character and I have to guesse it. First, think of a character from a cartoon, TV series, book, anime or film and just tell me his full name."

        try:
            genai_response = genai.generate(
                initial_prompt,
                [],
            )
        except Exception as exception:
            raise AppError("Failed to generate genai response") from exception

        history = genai.append_history([], initial_prompt, "user")
        history = genai.append_history(history, genai_response, "model")

        game = GameModel(character=genai_response, history=history, attempts=10)

        return game

    def handle_question(self, question: str, game: Dict) -> Tuple[str, GameModel]:
        self.__validate_question(question)

        self.__validate_game(game)

        character = game["character"]
        current_history = game["history"]

        prompt = f"""I'm trying to guess the character you just thought of. About {character} I ask you a question. Answer in up to 350 characters and do not mention {character} name in your answer under any circumstances. If I ask {character} name, you must say you can't do it... Don't answer with simple no or yes and do not repeat your previous answers. Also if I guess the name correctly in the following question you must congratulate me.
    
            The question is: '{question if question.endswith('?') else question + '?'}'"""

        genai_response = genai.generate(prompt, current_history)

        new_history = genai.append_history(current_history, prompt, "user")
        new_history = genai.append_history(new_history, genai_response, "model")

        return [
            genai_response,
            GameModel(
                history=new_history,
                character=game["character"],
                attempts=int(game["attempts"]),
            ),
        ]

    def __validate_question(self, question) -> None:
        if not isinstance(question, str):
            raise AppError("Invalid question", 400)

    def __validate_game(self, game) -> None:
        if (
            not isinstance(game["history"], list)
            or not isinstance(game["character"], str)
            or not int(game["attempts"])
        ):
            raise AppError("Invalid game", 400)
