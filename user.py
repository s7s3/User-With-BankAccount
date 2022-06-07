from bankaccount import BankAccount

class User:
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email
        self.account =[BankAccount(int_rate=0.02, balance=0)]
    def make_deposit(self, amount, account_num):	# takes an argument that is the amount of the deposit
        if account_num < len(self.account):
            self.account[account_num].balance += amount	# the specific user's account increases by the amount of the value received
        elif account_num == len(self.account):
            self.account += [BankAccount(int_rate=0.02, balance=0)]
            self.account[account_num].balance += amount
        else:
            print("wrong account num")
        return self
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount, account_num):
        if account_num < len(self.account):
            self.account[account_num].balance -= amount
        else:
            print("wrong account num")
        return self

    def display_user_balance(self, account_num):
        print(f"User: {self.name}, Account Number:{account_num}, Balance: ${self.account[account_num].balance}")
        return self
    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and 
    # add that amount to other other_user's balance
    def transfer_money(self, account_num, other_user, user_account_num, amount):
        if account_num < len(self.account) and user_account_num < len(other_user.account):
            other_user.account[user_account_num].balance += amount
            self.account[account_num].balance -= amount
        else:
            print("wrong account num")
        return self

hossam = User('hossam','hossam@gmail.com')
khlid = User('khlid', 'khir495@gmail.com')
ratyl = User('ratyl', 'rtyll87@gmail.com')

hossam.make_deposit(4000,1).make_deposit(2000,1).make_deposit(2000,0).make_withdrawal(300,1).display_user_balance(1)

khlid.make_deposit(220000,0).make_deposit(150,0).make_withdrawal(450,0).make_withdrawal(1500,0).display_user_balance(0)

ratyl.make_deposit(5000,0).make_withdrawal(2000,0).make_withdrawal(400,0).make_withdrawal(290,0).display_user_balance(0)

hossam.transfer_money(1, ratyl, 0, 1000).display_user_balance(1)
ratyl.display_user_balance(0)
