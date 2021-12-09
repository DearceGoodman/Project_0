from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account


class AccountDAOImp(AccountDAO):
    # NEED TO ADD PREMADE DATA FOR TESTS WHEN THEY ARE CREATED
    account_one = Account(1, 0, 0)
    account_two = Account(2, 0, 0)
    account_three = Account(3, 0, 0)
    account_four = Account(4, 0, 0)
    account_list = [account_one, account_two, account_three, account_four]
    account_id_generator = 5

    def create_account(self, account: Account) -> Account:
        new_account = account
        new_account.account_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(new_account)
        return new_account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

    def get_all_accounts(self) -> List[Account]:
        return AccountDAOImp.account_list

    def update_account_information(self, account: Account) -> Account:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account.account_id:
                return account_in_list

    def delete_account_information(self, account_id: int) -> bool:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                index = AccountDAOImp.account_list.index(account)
                del AccountDAOImp.account_list[index]
                return True

    def deposit_into_account_by_id(self, account: Account) -> Account:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account.account_id:
                index = AccountDAOImp.account_list.index(account_in_list)
                AccountDAOImp.account_list[index] = account
        return account

    def withdraw_from_account_by_id(self, account: Account) -> Account:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account.account_id:
                index = AccountDAOImp.account_list.index(account_in_list)
                AccountDAOImp.account_list[index] = account
        return account
