from .connection import Connection


class DataSource:
    def __init__(self, connection: Connection):
        self.connection = connection
