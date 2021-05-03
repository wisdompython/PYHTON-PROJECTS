class BankAccount:

    def __init__(self):
        self.balance = 0
    def account(self,account_number):
        name = account_number
        registered_accounts = [233456,566788,667777]
        if name in registered_accounts:
            return ('welcome, you are a valid user')
        else:
            return  ('invalid account')

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('insufficient funds')
    def print_balance(self):
        return self.balance
accounts = BankAccount()
account_number = int(input('what is you account number: '))
print(accounts.account(account_number))
accounts.deposit(500)
print(accounts.print_balance())