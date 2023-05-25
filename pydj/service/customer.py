from pydj.decorator import Service
from pydj.repository import CustomerRepository


@Service
class CustomerService:
    """This is a service for handling customers"""
    customer_repository: CustomerRepository

    def find_by_id(self, id: int) -> None:
        """Find customer by id

        Add some random comment here for fun!!!
        """
        print(f'{self.__class__.__name__}.find_by_id({id})')
        self.customer_repository.find_by_id(id)
