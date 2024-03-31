from typing import Dict, Tuple

from providers.genai_provider import GenAiProvider
from models.game_model import GameModel
from utils.app_error import AppError
from utils.hypescript import Hyperscript


genai = GenAiProvider()
hyperscript = Hyperscript()


class GameController:
    def start(self) -> GameModel:
        initial_prompt = "Let's play a guessing game like Akinator where you will think of a character and I will have to guess its name! First, think of a character from any cartoon, TV show, book, anime, manga, comic or movie, it can be a hero, villian or anti-hero whatever. Now, just tell me his full name for saving it in the context game."

        try:
            genai_response = genai.generate(
                initial_prompt,
                [],
            )

            history = genai.append_history([], initial_prompt, "user")
            history = genai.append_history(history, genai_response, "model")

            print(genai_response)

            game = GameModel(character=genai_response, history=history, attempts=15)

            return game
        except AppError as error:
            print(error)
            return AppError("Houve um problema ao iniciar o nosso jogo")

    def handle_question(self, question: str, current_game: Dict) -> Dict:
        try:
            game = self.__validate_game(current_game)

            character = game.character
            current_history = game.history
            attempts = game.attempts - 1

            if attempts == 0:
                template = hyperscript.create_element(
                    f"<span>You lose! The character was {character}! HAHAHAH!<span>",
                    "on load trigger click on #end-fail-game-alert-trigger then call htmx.ajax('GET', '/end', '#fail-message')",
                )
                return {
                    "template": template,
                    "genai_response": "",
                    "game": GameModel(
                        history=[],
                        character="",
                        attempts=attempts,
                    ),
                }

            self.__validate_question(question)

            prompt = f"""
            It's my turn! Let's see if I can guess the character you're thinking of. I'll ask you a question, but there are a few ground rules:

            You can't tell me the character's name, no matter what.
            Your answers should be short and sweet, under 300 characters.
            If I ask you directly for the name, you'll have to tell me you can't reveal it.
            I'd prefer unique answers each time, so try to avoid repeating yourself.
            I would appreciate it if your answers were complete and included some subtle hints.
            Simple yes or no answers won't help me guess.
            If I manage to guess the character correctly after a question, you'll declare victory with a "you win" message. Otherwise, the game continues!
        
            So, my question is: "{question if question.endswith('?') else question + '?'}"
            """

            genai_response = genai.generate(prompt, current_history)

            print(genai_response)

            new_history = genai.append_history(current_history, prompt, "user")
            new_history = genai.append_history(new_history, genai_response, "model")

            if "you win" in genai_response.lower():
                template = hyperscript.create_element(
                    f"<span>Congratulations! The character was {character}<span>",
                    "on load trigger click on #end-success-game-alert-trigger then call htmx.ajax('GET', '/end', '#success-message')",
                )
                return {
                    "template": template,
                    "genai_response": "",
                    "game": GameModel(
                        history=[],
                        character="",
                        attempts=attempts,
                    ),
                }

            template = hyperscript.create_element(
                genai_response,
                f"on load put {attempts} into #attempts",
                "span",
            )

            return {
                "template": template,
                "genai_response": genai_response,
                "game": GameModel(
                    history=new_history,
                    character=character,
                    attempts=attempts,
                ),
            }
        except AppError as error:
            return {"error": str(error)}

    def handle_last_game_state(self, request: Dict) -> Tuple[bool, str]:
        has_game = "last_genai_response" in request and request["last_genai_response"]

        last_genai_response = (
            request["last_genai_response"]
            if has_game
            else "I will think of character and you should guess its name correctly."
        )

        return (has_game, last_genai_response)

    def handle_end_game_attempts(self, attempts: int) -> str:
        return (
            "You guessed the character's name correctly! 🎉"
            if attempts > 0
            else "You couldn't get the character's name! 😭"
        )

    def __validate_question(self, question) -> None:
        if not isinstance(question, str):
            raise AppError("Invalid question", 400)

    def __validate_game(self, game) -> GameModel:
        if (
            not isinstance(game["history"], list)
            or not isinstance(game["character"], str)
            or not int(game["attempts"])
        ):
            print(game["attempts"])
            raise AppError("Invalid game", 400)

        return GameModel(
            history=game["history"],
            character=game["character"],
            attempts=int(game["attempts"]),
        )
