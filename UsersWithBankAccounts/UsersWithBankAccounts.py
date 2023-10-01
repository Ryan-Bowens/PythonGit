class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = 0.02
        self.balance = 100

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if (self.balance < amount):
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

class User:
    def __init__(self, fName, lName, email, age):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def display_info(self):
        print(self.fName, self.lName, self.email, self.age)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def display_user_balance(self):
        self.account.display_account_info()


c1 = User("Ryan", "Bowens", "bowensryan@gmail.com", 25)

c1.display_info()
c1.enroll()
print(c1.is_rewards_member, c1.gold_card_points)
c1.spend_points(20)
print(f"Remaining points: {c1.gold_card_points}")

c1.make_deposit(50)
c1.account.display_account_info()

ba1 = BankAccount