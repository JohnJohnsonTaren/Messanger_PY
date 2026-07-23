from exceptions import EmptyUsernameError, UserAlreadyExistsError, WeakPasswordError, InvalidCredentialsError


REGISTER_SUCCESS = "Реєстрація пройшла успішно"
LOGGING_SUCCESS = "Ви успішно увійшли"
EMPTY_USER_NAME = "Ім'я користувача не може бути порожнім!"
USER_ALREADY_EXIST = "Користувач з таким ім'ям вже існує!"
WEAK_PASSWORD = "Ваш пароль не відповідає  вимогам!"
INVALID_CREDS = "Ім'я користувача та/або пароль невірні"

class AuthController:

    def __init__(self, auth_service):
        self.auth_service = auth_service

    def handle_register(self, username, password):
        try:
            self.auth_service.register(username, password)
            return REGISTER_SUCCESS
        except EmptyUsernameError:
            return EMPTY_USER_NAME
        except UserAlreadyExistsError:
            return USER_ALREADY_EXIST
        except WeakPasswordError:
            return WEAK_PASSWORD

    def handle_login(self, username, password):
        try:
            self.auth_service.login(username, password)
            return LOGGING_SUCCESS
        except InvalidCredentialsError:
            return INVALID_CREDS

