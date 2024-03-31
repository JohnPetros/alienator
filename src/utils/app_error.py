from flask import abort


class AppError(BaseException):
    def __init__(
        self, message: str, status_code: int = 500, should_abort: bool = False
    ) -> None:
        print(message)

        if should_abort:
            abort(status_code, message)
