class AuthController:

    def __init__(self, auth_service):
        self.auth_service = auth_service

    def  handle_register(self, username, password):
        result = self.auth_service.register(username, password)
        if result:
            return "Реєстрація пройшла успішно."
        else:
            return "Помилка реєстрації."

    def handle_login(self, username, password):
        result = self.auth_service.login(username, password)
        if result:
            return "Ви успішно увійшли."
        else:
            return "Вхід не вдалий"