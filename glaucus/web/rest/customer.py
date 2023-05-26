from glaucus.service import CustomerService
from pydj.di.decorator import controller
from pydj.di.decorator.rest import get, rest


@controller()
@rest("/api")
class CustomerController:
    def __init__(self, customer_service: CustomerService):
        print('calling customer_controller.__init__')
        self.customer_service = customer_service

    @get("/customer")
    def get_customer(self) -> None:
        self.customer_service.find_by_id(1)

    @get("/customer/:id")
    def get_customer_by_id(self, id: int) -> None:
        self.customer_service.find_by_id(id)

    def __str__(self) -> str:
        return f"customer_controller: {self.__class__.__name__}"
