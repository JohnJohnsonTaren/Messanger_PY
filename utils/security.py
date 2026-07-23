import re
import bcrypt
from exceptions import WeakPasswordError

MIN_PASSWORD_LENGTH = 8
MIN_UPPERCASE_CHARS = 1
MIN_SPECIAL_CHARS = 1
MIN_DIGITS = 1

def hash_password(password):
    return bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('UTF-8'), hashed)

def validate_password(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        raise WeakPasswordError(f"Мінімум {MIN_PASSWORD_LENGTH} символів")
    if not re.search("[A-Z]", password):
        raise WeakPasswordError(f"Мінімум {MIN_UPPERCASE_CHARS} букв")
    if not re.search('[!@#$%^&*]', password):
        raise WeakPasswordError(f"Мінімум {MIN_SPECIAL_CHARS} спецсимвол")
    if not re.search('[0-9]', password):
        raise WeakPasswordError(f"Мінімум {MIN_DIGITS} цифра")


