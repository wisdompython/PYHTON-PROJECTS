class ATM:

    def __init__(self):
        self.balance = 0
    def account(self, account_number):
        name = account_number
        if len(name) == 12:
            return('welcome')
        else:
            return('invalid login, account number should be 12 digits!!!')
class operations:
    
    def operation1(self):
