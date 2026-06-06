class MessageRepository:

    def __init__(self, database):
        self.database = database

    def save_message(self, message):

        # TODO:
        # Сохранение сообщения
        pass

    def get_chat_history(self):

        # TODO:
        # Получение истории чата
        pass

    def get_private_history(
            self,
            sender,
            receiver
    ):

        # TODO:
        # Получение истории приватного чата
        pass