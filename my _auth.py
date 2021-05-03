# register
# - Username , password , Email Address
# set a recovery email

# generate user Account

import random
#login
#- Username and Password

# forget Password
# Generate a new password
ValidOption = False
def init():
    print('Welcome to WisBank')
    while ValidOption == False:
        Have_Account   = int(input('Do you have an account with us : 1(yes) 2(no)  '))
        if Have_Account == 1:
            ValidOption = True
            Login()
        elif Have_Account == 2:
            ValidOption = True
            Register()
        else:
            print('sorry, you have selected an invalid option')
def Login():
    print('This is a login Function')

def Register():
    username = input( 'Username : ' )
    password = input('password: ')
    email = input('Email Address: ')

def BankOperation():
    print('xv')

def GenerateAccountNum():
    print('welcome')
    return random.sample(range(0,10),10)

# init()

print(GenerateAccountNum())
