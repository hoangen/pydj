import logging

from ..db.datasource import DataSource
from ..domain import Customer

class CrudRepository:
    # def __init__(self, db: DataSource):
    #     print(f'init {self.__class__.__name__}')
    #     self.db = db

    # def find_by_id(self, id):
    #     return self.db.find(id)

    # def find_all(self):
    #     return self.db.find_all()

    # FIXME temporary skip bean decorator
    def __init__(self):
        logging.warning('calling CrudRepository.__init__')
        
    def find_by_id(self, id: int) -> Customer:
        return Customer(id=id, age=35, name='hoang', balance=2000.0, rate=1.5, address='Ho Chi Minh')
