class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount

    def get_balance(self):
        return self.balance
