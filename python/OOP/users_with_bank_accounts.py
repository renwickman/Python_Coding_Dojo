class User:
    def __init__(self, name, amount):
        self.name = name
        self.account1 = BankAccount(balance=amount)
        self.account2 = BankAccount(balance=amount)


    def make_deposit(self, amount):
        self.account1.deposit(amount)
        self.account2.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account1.withdraw(amount)
        self.account2.withdraw(amount)
        return self

    def display_user_balance (self):
        print(self.account1.display_account_info())
        print(self.account2.display_account_info())
        return self
    
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        print(self.amount)
        print(other_user.amount)
        return self

class BankAccount:
    def __init__(self, balance):
        self.int_rate = 0.10
        self.balance = balance
    
    def deposit(self, balance):
        self.balance += balance
        return self
    
    def withdraw(self, balance):
        self.balance -= balance
        return self
        
    def display_account_info(self):
        print(self.balance)
        return self
        
    def yield_interest(self):
        self.balance = (self.int_rate * self.balance) + self.balance
        print()
        return self



user1 = User("Jonathan", 3000)
user2 = User("Declan", 5000)
# user3 = User("Bob", 7000)


user1.account1.deposit(10000).display_account_info()
user1.account2.deposit(10000).withdraw(500).display_account_info()

# user2.make_deposit(200).make_deposit(200).display_user_balance()

# user3.make_deposit(600).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# user1.transfer_money(user3, 100)





# account1 = BankAccount(1000)
# account2 = BankAccount(1000)

# account1.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()
# account2.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()