from os import getenv
from typing import Dict
from typing import Literal
import google.generativeai as genai


class GenAiProvider:
    def __init__(self):
        genai.configure(api_key=getenv("GEMINI_API_KEY"))

        generation_config = {
            "temperature": 0.6,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        self.model = genai.GenerativeModel(
            model_name="gemini-1.0-pro",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

    def append_history(
        self, current_history, last_prompt, role: Literal["model", "user"] = "model"
    ) -> Dict:
        current_history.append(
            {"role": role, "parts": [last_prompt]},
        )

        return current_history

    def generate(self, prompt, history) -> str:
        convo = self.model.start_chat(history=history)

        user_prompt = {"role": "user", "parts": [prompt]}

        convo.send_message(user_prompt)

        return convo.last.text
