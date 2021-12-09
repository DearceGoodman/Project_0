from abc import ABC, abstractmethod

from entities.customer import Customer


class CustomerDAO(ABC):

    # create player method
    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # get player information
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass

    # get all player information
    @abstractmethod
    def get_all_customers_information(self) -> list[Customer]:
        pass

    # update player information
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    # delete player information
    @abstractmethod
    def delete_customer_information(self, customer_id: int) -> bool:
        pass
