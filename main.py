from pydj.repository.customer import CustomerRepository
from pydj.service.customer import CustomerService

if __name__ == '__main__':
    print('Welcome to python dependency injection')
    customer_repository = CustomerRepository()
    customer_service = CustomerService(customer_repository)

    customer_service.find_by_id(1)
