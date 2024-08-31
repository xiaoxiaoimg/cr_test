from bank import Bank
import math


def transfer(bank, from_acc_num, to_acc_num, amount):
    from_account = bank.get_account(from_acc_num)
    to_account = bank.get_account(to_acc_num)

    if from_account is None or to_account is None:
        raise ValueError("账户不存在")

    if isinstance(amount, (int, float)) and amount > 0:
        from_account.withdraw(amount)
        to_account.deposit(amount)
    else:
        raise ValueError("无效的交易金额")


def calculate_interest(bank, rate):
    import time

    time.sleep(1)  # 模拟利息计算过程
    for account in bank.accounts.values():
        interest = account.get_balance() * (rate / 100)
        account.deposit(interest)
