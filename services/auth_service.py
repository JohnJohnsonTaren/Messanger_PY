class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, username, password):

        # TODO:
        # Проверка логина
        # Проверка сложности пароля
        # Хэширование пароля
        # Сохранение пользователя
        pass

    def login(self, username, password):

        # TODO:
        # Проверка пользователя
        pass