class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        print(f"Deposited: ${amount}")
        self.balance += amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        print(f"Withdrew: ${amount}")
        if (self.balance < amount):
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def yield_interest(self):
        interest_gained = self.balance * self.int_rate
        print(interest_gained)
        self.balance += interest_gained * self.int_rate
        return self
    
    def display_account_info(self):
        print(f"Your Balance: {self.balance}")
        return self
    
ba1 = BankAccount(0.02, 100)
ba2 = BankAccount(0.02, 200)

ba1.display_account_info().deposit(50).deposit(50).deposit(50).withdraw(150).yield_interest().display_account_info()
print("----------")
ba2.display_account_info().deposit(25).deposit(75).withdraw(150).withdraw(50).withdraw(100).withdraw(80).yield_interest().display_account_info()