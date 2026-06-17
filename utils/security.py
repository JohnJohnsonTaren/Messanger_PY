import re
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('UTF-8'), hashed)

def validate_password(password):
    if len(password) >= 8 and re.search('[A-Z]', password) and re.search('[!@#$%^&*]', password) and re.search('[0-9]', password):
        return True
    else:
        print(f"\nВаш пароль{password} не відповідає вимогам: ")
        print("Мінімум 8 символів")
        print("Хочаб 1 велика літера")
        print("Хочаб один спецсимвол")
        print("Хочаб одну цифру")

        return False


