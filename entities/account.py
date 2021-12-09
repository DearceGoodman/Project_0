class Account:
    def __init__(self, account_id: int, account_balance: int, customer_id: int):
        self.account_id = account_id
        self.account_balance = account_balance
        self.customer_id = customer_id

    def __str__(self):
        return "AccountId: {}, Balance: {}, CustomerId: {}".format(self.account_id,
                                                                   self.account_balance,
                                                                   self.customer_id)

    def create_account_dictionary(self):
        return {
            "accountId": self.account_id,
            "accountBalance": self.account_balance,
            "customerId": self.customer_id
        }

    # is this necessary
    def __repr__(self):
        return "AccountId: {}, Balance: {}, CustomerId: {}".format(self.account_id,
                                                                   self.account_balance,
                                                                   self.customer_id)
