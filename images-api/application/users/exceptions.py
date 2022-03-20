from application.common.exceptions import HttpException


class UserException(HttpException):
    def __init__(self, code: int, message: str):
        super().__init__(code, message)


class UserNotFoundException(UserException):
    def __init__(self, user_login_or_id: str = ""):
        self.code = 404
        self.message = f"User {user_login_or_id} not found"
        super().__init__(404, self.message)


class IncorrectPasswordException(UserException):
    def __init__(self):
        self.code = 403
        self.description = "Incorrect password"
        super().__init__(self.code, self.description)


class LoginAlreadyExists(UserException):
    def __init__(self, login: str):
        self.code = 409
        self.description = f"Login {login} already exists"
        super().__init__(self.code, self.description)


class EmailAlreadyExists(UserException):
    def __init__(self, email: str):
        self.code = 409
        self.description = f"Email {email} already exists"
        super().__init__(self.code, self.description)
