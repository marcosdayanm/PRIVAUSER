import os
import platform
import time
from tabulate import tabulate
import prenc
from Accounts import Accounts
from ginput import get_input


def load_key():
    '''Function used to load the key from the file to a varible.'''
    return open("encryption.key", "rb").read()

def clearscreen():
    '''Function used to clear the terminal so the content printed can be better appreciated'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    return True


def incorrectnum(n, size):
    '''This function is for checking the user is entering the right parameters so don\'t causes the program to crash'''
    if n > size or n < 1:
        return True
    return False



def num1(accounts):
    '''This function works with the class Accounts and the module tabulate in order to print on the terminal a formatted table with the information of the account of the user'''
    acc_table = [['#', 'Site', 'Email', 'Username', 'Password']]
    acc_table = accounts[0].filltable(acc_table, len(accounts), accounts)
    return tabulate(acc_table, tablefmt='double_outline')


def num3():
    '''This function is called when the user wants to upload or modify an account, it asks the user for all the information for the account, and then creates an object with it to return it to the main program'''
    while True:
        site = get_input(str, 'Insert the site: ')
        email = get_input(str, 'Insert the email linked to your account: ')
        username = get_input(str, 'Insert the username of your account: ')
        password = get_input(str, 'Insert the password of your account: ')
        clearscreen()
        print(tabulate((['Site',site],['Email',email],['Username',username],['Password',password])))
        data_correct = get_input(int, 'Is all your data correct? Type 1 for yes and 2 for no: ')
        if data_correct == 1:
            clearscreen()
            return Accounts(site, email, username, password)
        else:
            x = get_input(int, 'Do you still want perform the operation? Type 1 for yes and 2 for no: ')
            if x == 1:
                continue
            return None


def num6(last, pwd1, pwd2):
    '''This function is for changing the master password, checks is the user inputted correctly the password comparing both attempts he made, and if it matches, it calls the method change pass of the prenc module that works with bcrypt'''
    
    if pwd1 == pwd2:
        prenc.change_pass(last, pwd1)
        return True
    else:
        return False



def save_file(file, key, object):
    '''This function is for saving the file each time it has a modification, so it anything happens, the information is perfectly stored and encrypted.'''
    '''This is one of the most important methods because it is in charge of keeping the information safe. t decifers the file, to then write the information of the accounts with the help of the class, to then cifer it again, all this process happens on matter of miliseconds so the infromation is kept safe'''
    prenc.decrypt_file(file, key)
    Accounts.write_accounts(file, object)
    prenc.encrypt_file(file, key)

    

def main():

    '''Verifying the master password to enter the system'''
    if not prenc.enter_the_system():
        return False

    '''Saving the encryption key for the personal information file on a variable'''
    key = load_key()
    accountsfile = 'accounts.csv'


    '''Decryption of the file and saving it on a class to show the user its information'''
    prenc.decrypt_file(accountsfile, key)
    accounts = Accounts.read_accounts('accounts.csv')
    prenc.encrypt_file(accountsfile, key)

    '''Menu that will be displayed with the tabulate module'''
    menu = [
            ['1','See my saved accounts'],
            ['2','Change the displaying time of the accounts'],
            ['3','Upload a new account'],
            ['4','Modify an existant account'],
            ['5','Delete an existant account'],
            ['6','Change my master password'],
            ['7','Exit the program']
                ]

    t_dis_1 = 5

    while True:
        '''This is a loop that administrates the integration of all the modules, methods and functions to work properly and to be called on the exact time to satisfy the user\'s needs'''
        clearscreen()
        print('\nWelcome to your Accounts Vault, please choose the option you would like to perform:\n')
        print(tabulate(menu, tablefmt='double_outline'))

        num = get_input(int, 'Insert the number of your choice: ')
        
        clearscreen()
        '''This conditional control structure calls the function the user is asking for and filfill its needs'''
        if num == 1:
            print(num1(accounts))
            time.sleep(t_dis_1)

        elif num == 2:
            print('Because of security, the default time of displaying your accounts dashboard is of 5 seconds')
            t_dis_1 = get_input(float, 'Insert the amount of seconds you want your dashboard to be displayed: ')

        elif num == 3:
            obj = num3()
            if obj:
                accounts.append(obj)
                save_file(accountsfile, key, accounts)
        
        elif num == 4:
            print(num1(accounts))
            number = get_input(int, 'Which account do you want to modify? ')
            if incorrectnum(number, len(accounts)):
                print('\nThe number of the account you tyoed does not exist. Try again\n')
                time.sleep(2)
                continue

            obj = num3()
            if obj:
                accounts[number-1] = obj
                save_file(accountsfile, key, accounts)
        
        elif num == 5:
            print(num1(accounts))
            number = get_input(int, 'Which account do you want to delete? ')
            if incorrectnum(number, len(accounts)):
                print('\nThe number of the account you tyoed does not exist. Try again\n')
                time.sleep(2)
                continue

            sure = get_input(int, 'Are you sure? This process cannot be reversed, type 1 for yes and 2 for no: ')
            if sure == 1:
                del accounts[number-1]
            else:
                print('\nAction interrupted, redirecting to the menu\n')
                time.sleep(1)
            
        elif num == 6:
            last = get_input(str, 'Insert the current master password you want to change: ')
            if not prenc.check_pass(last):
                print('\nIncorrect password, in order to change your master password you must enter the current one, try again\n')
                time.sleep(2)
                continue
            pwd1 = get_input(str, '\nInsert the new master password: ')
            pwd2 = get_input(str, 'Insert the new master password again: ')
            if not num6(last, pwd1, pwd2):
                print('\nThere was a problem changing your master password, try again\n')
                time.sleep(2)
                continue
            print('\n\nCifred master password changed and saved on the system\n\n')
            time.sleep(2)
        
        elif num == 7:
            save_file(accountsfile, key, accounts)
            print('\n\nYour information has been succesfully ecrypted\nExiting the program...\n\n')
            time.sleep(2)
            clearscreen()
            break
        
        else:
            print('\nInvalid input, try again\n')
            time.sleep(2)
        
        continue
    



if __name__ == '__main__':
    main()