def main():
    print("Всем привет, это командный мини проэкт. Всем рады!")

from controllers.auth_controller import AuthController
from views.login_view import LoginView

def main():

    view = LoginView()
    controller = AuthController(view)

    controller.start()

if __name__ == "__main__":
    main()

