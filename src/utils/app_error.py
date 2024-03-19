from flask import abort


class AppError(BaseException):
    def __init__(self, message: str, status_code: int = 500) -> None:
        print(message)
        abort(status_code, message)
