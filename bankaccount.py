class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = float(int_rate)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount 
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.int_rate > 0:
            self.balance += (self.balance * self.int_rate)
        return self

account1 = BankAccount(0.05, 5000)
account2 = BankAccount(0.01, 2000)

account1.deposit(400).deposit(3500).deposit(1200).withdraw(500).yield_interest().display_account_info()
account2.deposit(300).deposit(900).withdraw(1500).withdraw(150).withdraw(320).withdraw(30).yield_interest().display_account_info()