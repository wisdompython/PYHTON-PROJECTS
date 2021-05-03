# register
# - Username , password , Email Address
# set a recovery email

# generate user Account

import random
import time
import sys
import time

#login
#- Username and Password

# forget Password
# Generate a new password


database = {}# dicitonary

def init():
    print('Welcome to WisBank')
    ValidOption = False

    while ValidOption == False:

        Have_Account   = int(input('Do you have an account with us : 1(yes) 2(no)  '))

        if Have_Account == 1:
            ValidOption = True


            login()

        elif Have_Account == 2:
            ValidOption = True


            print(register())
        else:
            print('sorry, you have selected an invalid option')
            init()
def login():
    print("*****LOGIN******")

    isLogin = False

    while isLogin == False:

        time.sleep(2)

        account_no_user = int(input('input your account number : '))
        password = input("Password: ")

        for accountNumber, userinfo in database.items():
            if (accountNumber == account_no_user):
                if (userinfo[3] == password):
                    isLogin == True

                    print('logging in........................')
                    time.sleep(4)

                    print('Login is successful\n'
                          'Welcome', database[accountNumber][0])
                    sys.exit()

            else:
                isLogin == False
                print('Invalid Login info!!')


def register():
    print("******register*****")

    email = input('what is your Email Address: ')
    first_name = input( "what is your first name: " )
    last_name = input('what is your last name: ')
    password = input('Password:')

    accountNumber = GenerateAccountNum()
    print(accountNumber)

    database[accountNumber] = [ first_name , last_name, email, password]

    time.sleep(5)

    login()



def GenerateAccountNum():

    return random.randrange(1111111111,9999999999)


init()