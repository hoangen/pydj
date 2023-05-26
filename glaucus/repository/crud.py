from ..db.datasource import DataSource


class CrudRepository:
    def __init__(self, db: DataSource):
        print(f'init {self.__class__.__name__}')
        self.db = db

    def find_by_id(self, id):
        return self.db.find(id)

    def find_all(self):
        return self.db.find_all()
