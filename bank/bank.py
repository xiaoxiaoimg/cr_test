from account import Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        assert isinstance(account, Account), "必须为Account类的实例"
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
