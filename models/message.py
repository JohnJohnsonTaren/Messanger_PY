class Message:

    def __init__(
            self,
            sender,
            receiver,
            text,
            timestamp
    ):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.timestamp = timestamp