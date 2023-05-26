from db.connection import Connection
from db.datasource import DataSource

from pydj.di.decorator import bean, configuration


@configuration
class AppConfiguration:
    def __init__(self):
        pass

    @bean
    def datasource(self, connection: Connection):
        return DataSource(connection)

    @bean
    def connection(self):
        return Connection(
            url='http://example.com',
            username='hoang',
            password='secret'
        )
