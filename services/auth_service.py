from utils.security import hash_password, verify_password
from models.user import User


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, username, password):
        if not username.strip():
            print("Логін не може бути порожнім")
            return False
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            print("Користувач з таким логіном вже існує")
            return False

        password_hash = hash_password(password)
        user = User(id = None, username = username, password_hash = password_hash)
        self.user_repository.save(user)
        return True

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

