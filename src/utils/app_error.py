from flask import abort


class AppError(BaseException):
    def __init__(self, error: str, status_code: int = 500) -> None:
        abort(status_code, error)
