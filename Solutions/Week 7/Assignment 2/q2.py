import random


class Bank:
    def __init__(self):
        self.account_holder_name = input("Enter account holder's name: ")
        self.account_number = random.randint(100000, 999999)
        self.balance = 100.0
        self.account_type = input("Enter account type (Savings/Checking): ")

    def displayAllInfo(self):
        print("Bank Account Information:")
        print(f"Account Holder's Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Account Type: {self.account_type}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def getBalance(self):
        return self.balance


if __name__ == "__main__":
    bank_account = Bank()

    bank_account.displayAllInfo()

    bank_account.deposit(50.0)
    bank_account.withdraw(30.0)

    print(f"Current Balance: {bank_account.getBalance()}")
