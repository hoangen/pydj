import logging

from glaucus.service import CustomerService
from pydj.di.decorator import controller
from pydj.di.decorator.rest import get, rest

from ...domain import Customer


@controller()
@rest('/api')
class CustomerController:
    def __init__(self, customer_service: CustomerService):
        logging.warning('calling CustomerController.__init__')
        self.customer_service = customer_service

    @get('customer')
    def get_customer(self) -> Customer:
        return self.customer_service.find_by_id(1)

    @get('/customer/:id')
    def get_customer_by_id(self, id: int) -> Customer:
        return self.customer_service.find_by_id(id)

    def __str__(self) -> str:
        return f'customer_controller: {self.__class__.__name__}'
