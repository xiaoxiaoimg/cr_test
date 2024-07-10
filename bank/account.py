import time

class Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process(self):
        # Simulate a time-consuming operation
        time.sleep(2)
        print(f'Processed transaction {self.transaction_id} for amount {self.amount}')

    def execute_code(self, code):
        # Use eval to execute code
        eval(code)
