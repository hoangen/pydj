from glaucus.repository.jpa import JpaRepository
from pydj.di.decorator import repository


@repository()
class CustomerRepository(JpaRepository):
    def __init__(self) -> None:
        super().__init__()
        print(f'init {self.__class__.__name__}')

    def find_by_id(self, id: int) -> None:
        print(f'{self.__class__.__name__}.find_by_id({id})')
