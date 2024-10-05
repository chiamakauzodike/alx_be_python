#bank_account.py
class BankAccount:
    def __init__(self, account_balance, initial balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print(f"deposit successful: ${amount:}")
        else:
            print("Deposit require positive value")

    def withdraw(self, amount):
        if amount > self.initial_balance:
            return False
        elif amount > 0:
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current bance: ${self.initial_balance}"
