from abc import ABC, abstractmethod

from entities.customer import Customer


class CustomerService(ABC):

    # create player method
    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass

    @abstractmethod
    def service_update_customer(self, customer: Customer) -> Customer:
        pass
