from database.database_interface import DatabaseInterface


class SQLiteAdapter(DatabaseInterface):

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):

        # TODO:
        # Реализовать подключение к SQLite
        pass

    def execute(self, query, params=None):

        # TODO:
        # Выполнение SQL запроса
        pass

    def close(self):

        # TODO:
        # Закрытие соединения
        pass