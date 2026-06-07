from database.database_interface import DatabaseInterface


class PostgreSQLAdapter(DatabaseInterface):

    def connect(self):

        # TODO:
        # Подключение к PostgreSQL
        pass

    def execute(self, query, params=None):

        # TODO:
        # Выполнение запроса
        pass

    def close(self):

        pass