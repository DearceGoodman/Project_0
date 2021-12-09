from abc import ABC, abstractmethod
from typing import List

from entities.account import Account


class AccountDAO(ABC):

    # create Account
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # get Account
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    # get all Accounts
    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    # update team
    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    # delete team
    @abstractmethod
    def delete_account_information(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account: Account) -> bool:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account: Account) -> Account:
        pass
