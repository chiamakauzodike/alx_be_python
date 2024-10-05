#bank_account.py
class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print(f"Deposited: ${amount:}")
        else:
            print("Deposit require positive value")

    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("Insufficient funds.")
            return False
        elif amount > 0:
            self.initial_balance -= amount
            print(f"Withdrew: ${amount:}")
            return True
        else:
            print("Withdrawal amount should be positive")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.initial_balance}")
