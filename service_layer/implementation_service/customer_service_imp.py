from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.abstract_service.customer_service import CustomerService

"""
we are going to make use of dependency injection with our service class. This allows us to easily change the
implementation of our code by switching out the implementing class. Switching from a local to a cloud based database?
just pass in a cloud based implementation object into the service layer instead of a local based implementation object
"""


# BUSINESS LOGIC: players should have unique jersey numbers on the same team

class CustomerServiceImp(CustomerService):
    def __init__(self, customer_dao):
        # we are doing dependency injection with this init dunder method
        self.customer_dao: CustomerDAOImp = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        # need to implement business logic
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer.customer_id:
                raise DuplicateJerseyNumberException("Customer Id is already taken!")
            else:
                return self.customer_dao.create_customer_entry(customer)

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    def service_get_all_customers(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()

    def service_update_customer(self, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.customer_id == customer.customer_id:
                raise DuplicateJerseyNumberException("Customer Id is already taken!")
        return self.customer_dao.update_customer_information(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
