from abc import ABC, abstractmethod
from typing import List

from entities.account import Account


class AccountService(ABC):

    # create account
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # get account
    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    # get all account
    @abstractmethod
    def service_get_all_account(self) -> List[Account]:
        pass

    # update account
    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    # delete account
    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_deposit(self, account_id: int, deposit: int):
        pass

    @abstractmethod
    def service_withdraw(self, account_id: int, withdraw: int):
        pass
