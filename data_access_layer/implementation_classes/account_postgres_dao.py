from typing import List

from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDAO):

    def create_account(self, account: Account) -> Account:
        sql = "insert into account values(default, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_balance, account.customer_id])
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

    def get_all_accounts(self) -> List[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        accounts = []
        for account in account_records:
            accounts.append(Account(*account))
        return accounts

    def update_account_information(self, account: Account) -> Account:
        sql = "update account set account_balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_balance, account.account_id))
        connection.commit()
        return account

    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    def deposit_into_account_by_id(self, account: Account) -> Account:
        sql = "update account set account_balance= %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_balance, account.account_id))
        connection.commit()
        return account

    def withdraw_from_account_by_id(self, account: Account) -> Account:
        sql = "update account set account_balance= %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_balance, account.account_id))
        connection.commit()
        return account
