from pydj.di.decorator import controller, get
from pydj.service import CustomerService


@controller("/api")
class CustomerApi:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    @get("/customers")
    def get_all(self) -> None:
        self.customer_service.find_by_id(1)
