# this is a budget
class Budget:
    def __init__(self,category,amount):
        self.balance = 0 + amount
        self.category = category
        self.amount = amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('insufficient funds')
    def transfer_between_categories(self,cat_1,cat_2, amount):
        self.cat_1 = cat_1
        self.cat_2 = cat_2
        if self.balance > amount:
            self.balance = self.balance + amount
            return self.balance
        else:
            print('insufficient funds')
    def print_balance(self):
        return self.balance

category_1 = Budget('food', 1000)
category_2 = Budget('clothing', 2000)
category_1.deposit(500)
category_2.deposit(200)
category_2.transfer_between_categories('food','clothing',100)
print(category_2.print_balance())
print(category_1.print_balance())