# Inheritance Override
class Account:
    def __init__(self, name, number, balance):
        self.acc_name = name
        self.acc_number = number
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        if amount > self.acc_balance:
            print(f"Insufficient funds. Balance is {self.acc_balance}")
        else:
            self.acc_balance -= amount

    def __str__(self):
        return f"name: {self.acc_name}, accNo: {self.acc_number}, balance: {self.acc_balance}"


class DollarAccount(Account):
    def rates(self):
        return 153.89

    def deposit(self, amount):
        usd = amount / self.rates()
        self.acc_balance += usd


dc1 = DollarAccount("Jerry", "d001", 20000)
dc1.deposit(500)
print(dc1.acc_balance)
print(dc1.rates())
dc1.deposit(20000)
print(round(dc1.acc_balance, 2))

# acc1 = Account("Jude", "001", 10000)
# acc1.withdraw(2000)
# print(acc1)

# acc2 = Account("Henrik", "002", 14000)
# acc2.deposit(600)
# print(acc2.acc_balance)
