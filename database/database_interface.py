from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query, params=None):
        pass

    @abstractmethod
    def close(self):
        pass