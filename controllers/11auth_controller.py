from services.auth_service import AuthService


class AuthController:

    def __init__(self, view):

        self.view = view

        # В будущем внедряется через DI
        self.service = None

    def start(self):

        self.view.show()

    def login(self):

        username = self.view.get_login()
        password = self.view.get_password()

        # TODO:
        # Вызвать сервис авторизации
        pass

    def register(self):

        username = self.view.get_login()
        password = self.view.get_password()

        # TODO:
        # Вызвать регистрацию
        pass