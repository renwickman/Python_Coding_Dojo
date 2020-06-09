class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        

    def make_deposit(self,amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance (self):
        print(self.amount)
        return self
    
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        print(self.amount)
        print(other_user.amount)
        return self

user1 = User("Jonathan", 3000)
user2 = User("Declan", 5000)
user3 = User("Bob", 7000)

user1.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(500).display_user_balance()

user2.make_deposit(200).make_deposit(200).display_user_balance()

user3.make_deposit(600).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

user1.transfer_money(user3, 100)