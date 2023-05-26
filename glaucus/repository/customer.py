import logging

from glaucus.repository.crud import CrudRepository
from pydj.di.decorator import repository

from ..db.datasource import DataSource


@repository(scope="singleton")
class CustomerRepository(CrudRepository):
    # def __init__(self, db: DataSource) -> None:
    #     super().__init__(db)
    #     print(f'init {self.__class__.__name__}')

    # FIXME temporary skip bean decorator
    def __init__(self, timeout: int = 5) -> None:
        logging.warning('calling CustomerRepository.__init__')
        super().__init__()
        self.timeout = timeout
