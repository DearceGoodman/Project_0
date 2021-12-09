from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer
from service_layer.abstract_service.customer_service import CustomerService


class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    # need to check and make sure players do not have the same jersey number
    def service_create_customer(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for existing_customer in customers:
            if existing_customer.customer_id == customer.customer_id:
                raise DuplicateJerseyNumberException("Account is already taken!")
        created_customer = self.customer_dao.create_customer_entry(customer)
        return created_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    def service_get_all_customers(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()

    # need to check and make sure players do not have the same jersey number
    def service_update_customer(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for current_customer in customers:
            if current_customer.customer_id == customer.customer_id:
                raise DuplicateJerseyNumberException("Account Id is already taken!")
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
