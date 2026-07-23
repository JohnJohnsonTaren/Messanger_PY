from utils.security import hash_password, verify_password, validate_password
from models.user import User
from exceptions import UserAlreadyExistsError, EmptyUsernameError, InvalidCredentialsError


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, username, password):
        if not username.strip():
            raise EmptyUsernameError("Ім'я користувача не може бути порожнім")

        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise UserAlreadyExistsError("Користувач з таким ім'ям вже існує")
        validate_password(password)
        password_hash = hash_password(password)
        user = User(id = None, username = username, password_hash = password_hash)
        self.user_repository.save(user)
        return True

    def login(self, username, password):
        existing_user = self.user_repository.find_by_username(username)
        if not existing_user:
            raise InvalidCredentialsError("Ім'я користувача та/або пароль невірні")
        else:
            if verify_password(password, existing_user.password_hash):
                return True
            else:
                raise InvalidCredentialsError("Ім'я користувача та/або пароль невірні")


