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

account1 = BankAccount(3000)
account2 = BankAccount(5000)

account1.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()
account2.deposit(500).deposit(500).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()