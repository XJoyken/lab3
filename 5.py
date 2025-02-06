class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        print(f"{self.owner}: {self.balance} (after deposit)")
    def withdraw(self, wtd):
        if(self.balance - wtd >= 0):
            self.balance -= wtd
            print(f"{self.owner}: {self.balance} (after withdrawal)")
        else:
            print("insufficient funds in the balance")

a1 = Account(str(input("Name: ")), int(input("Balance: ")))
a1.deposit(int(input("Deposit operation: ")))
a1.withdraw(int(input("Withdrawal operation: ")))

a2 = Account(str(input("Name: ")), int(input("Balance: ")))
a2.deposit(int(input("Deposit operation: ")))
a2.withdraw(int(input("Withdrawal operation: ")))
a2.deposit(int(input("Deposit operation: ")))
a2.withdraw(int(input("Withdrawal operation: ")))