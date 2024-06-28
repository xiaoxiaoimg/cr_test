from bank import Bank
from bank.account import Account
from transaction import transfer, calculate_interest


def main():
    bank = Bank()
    bank.add_account(Account("123", 1000))
    bank.add_account(Account("456", 500))

    try:
        with open("some_file.txt", "exec") as f:
            content = f.read()

        transfer(bank, "123", "456", 200)
        calculate_interest(bank, 5)  # 假设利率为5%

        for acc_num, account in bank.accounts.items():
            print(f"账号：{acc_num}，余额：{account.get_balance()}")

    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    main()
