from _datetime import datetime
import time
print('Welcome to Zuri Bank')
name = input('input username: \n')
account_num = int(input('please input your account number:  '))
AllowedAccounts = [2345677, 4567890 , 345678]
AllowedPin = [1245, 3456, 9054]
if account_num in AllowedAccounts:
    print('welcome'+ name)
    userId = AllowedAccounts.index(account_num)
    Pin = int(input('input your Pin: '))
    if Pin == AllowedPin[userId]:
        print('loading......................')
        time.sleep(2.0)
        print('you are valid user')
else:
    print('invalid account, try again!!')
print(str(datetime.now()))
time.sleep(5.0)
operation = int(input('Kindly choose what operation you want to perform: \n  '
                  'to withdraw = input 1 \n'
                  'to deposit = input 2 \n'
                  'to check balance = input 3 \n'
                  'to make a complaints = input 4 \n' ))
if operation == 1:
    AccountBalances = [25000, 50000, 23000]
    UserBal = AccountBalances[userId]
    withdraw = int(input('how much would you like to withdraw: \n'))

    UserBal = AccountBalances[userId] - withdraw
    if withdraw < UserBal:
        print('Take your cash')
        print('your remaining balance is ', UserBal)
        print('Thank you for banking with us' + name)
    else :
        withdraw > UserBal
        print('Insufficient Balance')
        print('Thank you for banking with us' + name)

if operation == 2:
    AccountBalances = [25000, 50000, 23000]
    UserBal = AccountBalances[userId]
    deposit = int(input(' How much would you like to deposit: '))
    print('Transaction Successful')
    UserBal = AccountBalances[userId] + deposit
    print('your balance is ', UserBal )
    print('Thank you for banking with us' + name)

if operation == 3:
    AccountBalances = [25000, 50000, 23000]
    UserBal = AccountBalances[userId]
    print(UserBal)
    print('Thank you for banking with us' + name)

if operation == 4:
    Complaint = input(' What issue would you like to report: \n ')
    print('Thank You for contacting us')




