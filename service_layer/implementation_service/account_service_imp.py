from typing import List

from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account
from service_layer.abstract_service.account_service import AccountService


class AccountServiceImp(AccountService):
    def service_deposit(self, account_id: int, deposit: int):
        account = self.account_dao.get_account_by_id(account_id)
        account.account_balance += deposit
        return self.account_dao.update_account_information(account)

    def service_withdraw(self, account_id: int, withdraw: int):
        account = self.account_dao.get_account_by_id(account_id)
        account.account_balance -= withdraw
        return self.account_dao.update_account_information(account)

    # business logic: teams must not have the same name

    def __init__(self, account_dao: AccountDAOImp):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account_id == account.account_id:
                raise DuplicateTeamNameException("Account ID already in use")
        new_account = self.account_dao.create_account(account)
        return new_account

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_get_all_account(self) -> List[Account]:
        return self.account_dao.get_all_accounts()

    def service_update_account_information(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account_id != account.account_id:
                raise DuplicateTeamNameException("Account ID already in use")
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)
