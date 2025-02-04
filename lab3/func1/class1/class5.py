class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.amount += amount
        print(f"Depostied{amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


acc = Account("Давид", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200) 