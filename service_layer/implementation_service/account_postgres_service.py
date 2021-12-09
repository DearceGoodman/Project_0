from typing import List

from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account
from service_layer.abstract_service.account_service import AccountService


class AccountPostgresService(AccountService):
    def __init__(self, account_dao):
        # we are doing dependency injection with this init dunder method
        self.account_dao: AccountDAOImp = account_dao

    def service_create_account(self, account: Account) -> Account:
        for current_account in self.account_dao.account_list:
            if current_account.account_id == account.account_id:
                raise DuplicateJerseyNumberException("Account Id is already taken!")
            else:
                return self.account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    def service_get_all_account(self) -> List[Account]:
        pass

    def service_update_account_information(self, account: Account) -> Account:
        pass

    def service_delete_account_information(self, account_id: int) -> bool:
        pass