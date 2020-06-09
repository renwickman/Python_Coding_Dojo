class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def make_deposit(self,amount):
        self.amount += amount

    def make_withdrawal(self,amount):
        self.amount -= amount

    def display_user_balance (self):
        print(self.amount)
    
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        print(self.amount)
        print(other_user.amount)

user1 = User("Jonathan", 3000)
user2 = User("Declan", 5000)
user3 = User("Bob", 7000)

user1.make_deposit(500)
user1.make_deposit(500)
user1.make_deposit(500)
user1.make_withdrawal(500)
# user1.display_user_balance()

user2.make_deposit(200)
user2.make_deposit(200)
# user2.display_user_balance
# user2.display_user_balance

user3.make_deposit(600)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
# user3.display_user_balance

user1.transfer_money(user3, 100)