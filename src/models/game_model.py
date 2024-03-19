from typing import Dict


class GameModel:
    def __init__(self, character: str, history: list[Dict], attempts: int) -> None:
        self.character = character
        self.history = history
        self.attempts = attempts
