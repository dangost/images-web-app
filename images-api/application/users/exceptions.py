from application.common.exceptions import HttpException


class UserException(HttpException):
    def __init__(self, code: int, message: str):
        super().__init__(code, message)


class UserNotFoundException(UserException):
    def __init__(self, user_login_or_id: str = ""):
        self.code = 404
        self.message = f"User {user_login_or_id} not found"
        super().__init__(404, self.message)


class IncorrectCreditsException(UserException):
    def __init__(self):
        self.code = 403
        self.message = "Incorrect login or password"
        super().__init__(self.code, self.message)


class LoginAlreadyExists(UserException):
    def __init__(self, login: str):
        self.code = 409
        self.message = f"Login {login} already exists"
        super().__init__(self.code, self.message)


class InvalidLoginException(UserException):
    def __init__(self, login: str):
        self.code = 400
        self.message = f"Invalid login {login}"
        super().__init__(self.code, self.message)


class EmailAlreadyExists(UserException):
    def __init__(self, email: str):
        self.code = 409
        self.message = f"Email {email} already exists"
        super().__init__(self.code, self.message)
