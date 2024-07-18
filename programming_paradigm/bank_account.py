class BankAccount:
    def __init__(self, account_balance, amount):
        self.amount = amount
        self.account_balance = account_balance

    def deposit(self):
        self.account_balance += self.amount
        return self.account_balance

    def withdraw(self):
        if (self.account_balance - self.amount) > 0:
            self.account_balance -= self.amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}. Thank you!")

