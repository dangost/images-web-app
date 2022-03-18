class HttpException:
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message


class UnauthorizedException(HttpException):
    def __init__(self):
        super().__init__(401, "Unauthorized")
