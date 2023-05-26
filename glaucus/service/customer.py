from glaucus.repository import CustomerRepository
from pydj.di.decorator import service


@service()
class CustomerService:
    """This is a service for handling customers"""

    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def find_by_id(self, id: int) -> None:
        """Find customer by id

        Add some random comment here for fun!!!
        """
        print(f'{self.__class__.__name__}.find_by_id({id})')
        self.customer_repository.find_by_id(id)
