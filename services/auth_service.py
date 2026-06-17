from utils.security import hash_password, verify_password, validate_password
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
        if not validate_password(password):
            return False
        password_hash = hash_password(password)
        user = User(id = None, username = username, password_hash = password_hash)
        self.user_repository.save(user)
        return True

    def login(self, username, password):
        existing_user = self.user_repository.find_by_username(username)
        if not existing_user:
            return False
        else:
            if verify_password(password, existing_user.password_hash):
                return True
            else:
                print(f"Логін або пароль невірні")
                return False


