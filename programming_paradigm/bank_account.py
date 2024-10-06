#bank_account.py
class BankAccount:
    def __init__(self,initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit require positive value")

    def withdraw(self, amount):
        if amount > self._account_balance:
            print("Insufficient funds.")
            #return False
        elif amount > 0:
            self._account_balance -= amount
            print(f"Withdrew: ${amount}")
            #return True
        else:
            print("Withdrawal amount should be positive")
            #return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")
