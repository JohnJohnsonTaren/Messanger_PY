class ChatController:

    def __init__(
            self,
            chat_view,
            message_service
    ):
        self.chat_view = chat_view
        self.message_service = message_service

    def send_message(self):

        # TODO:
        # Получить текст из View
        # Передать в Service
        pass

    def send_private_message(self):

        # TODO:
        # Отправка приватного сообщения
        pass

    def load_history(self):

        # TODO:
        # Загрузка истории сообщений
        pass