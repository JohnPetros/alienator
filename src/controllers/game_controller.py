from typing import Dict

from providers.genai_provider import GenAiProvider
from models.game_model import GameModel
from utils.app_error import AppError
from utils.hypescript import Hyperscript


genai = GenAiProvider()
hyperscript = Hyperscript()


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

        game = GameModel(character=genai_response, history=history, attempts=15)

        return game

    def handle_question(self, question: str, current_game: Dict) -> Dict:
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
                "genai_response": template,
                "game": GameModel(
                    history=[],
                    character="",
                    attempts=attempts,
                ),
            }

        self.__validate_question(question)

        prompt = f"""I'm trying to guess the character's name you just thought of. About {character} I will ask you a question. You should answer in 200 characters and do not mention {character} name in your answer under any circumstances. If I ask {character} name, you must say you can't do it... Don't answer with simple no or yes and do not repeat your previous answers.
    
        My question is: '{question if question.endswith('?') else question + '?'}'
        
        If my question has the name of {character} you must congratulate me and the congratulations message you must put "you win" word. 
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
                "genai_response": template,
                "game": GameModel(
                    history=[],
                    character="",
                    attempts=attempts,
                ),
            }

        template = hyperscript.create_element(
            genai_response,
            f"on load put {attempts - 1} into #attempts",
            "span",
        )

        return {
            "genai_response": template,
            "game": GameModel(
                history=new_history,
                character=character,
                attempts=attempts - 1,
            ),
        }

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
        else:
            return GameModel(
                history=game["history"],
                character=game["character"],
                attempts=int(game["attempts"]),
            )
