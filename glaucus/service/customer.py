import logging

from glaucus.repository import CustomerRepository
from pydj.di.decorator import service

from ..domain import Customer


@service()
class CustomerService:
    """This is a service for handling customers"""

    def __init__(self, customer_repository: CustomerRepository):
        logging.warning('calling CustomerService.__init__')
        self.customer_repository = customer_repository

    def find_by_id(self, id: int) -> Customer:
        """Find customer by id

        Add some random comment here for fun!!!
        """
        print(f'{self.__class__.__name__}.find_by_id({id})')
        return self.customer_repository.find_by_id(id)
