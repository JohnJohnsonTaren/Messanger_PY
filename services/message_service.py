class MessageService:

    def __init__(self, repository):
        self.repository = repository

    def send_public_message(
            self,
            sender,
            text
    ):

        # TODO:
        # Создать объект Message
        # Отправить в общую комнату
        # Сохранить в БД
        pass

    def send_private_message(
            self,
            sender,
            receiver,
            text
    ):

        # TODO:
        # Отправка приватного сообщения
        pass