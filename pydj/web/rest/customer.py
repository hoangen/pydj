from pydj.decorator import Get, Rest
from pydj.service import CustomerService


@Rest("/api")
class CustomerApi:
    customer_service: CustomerService

    @Get("/customers")
    def get_all(self) -> None:
        self.customer_service.find_by_id(1)
