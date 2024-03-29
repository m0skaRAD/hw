class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, overdraft_fee):
        super().__init__(balance, owner)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds. Overdraft fee will be applied.")
            self.balance -= self.overdraft_fee

class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, interest_rate):
        super().__init__(balance, owner)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance *= (1 + self.interest_rate)


ch = CheckingAccount(100, "Maxim", 20)
ch.withdraw(50)
print(f"Checking account balance: {ch.balance}")

sa = SavingsAccount(500, "Stepan", 0.05)
sa.add_interest()
print(f"Savings account balance after interest: {sa.balance}")