import bcrypt
'''https://pypi.org/project/bcrypt/'''
from cryptography.fernet import Fernet
'''https://pypi.org/project/cryptography/'''



"""def generate_key():
    '''Generate a key for encryption and save it into a file. It was only necessary to call it once, to create the key used to cipher and decipher the csv file that contains the accounts'''
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)"""


def encrypt_file(fl, key):
    '''Encrypt a file using cryptography.fernet'''
    f = Fernet(key)
    with open(fl, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(fl, "wb") as file:
        file.write(encrypted_data)



def decrypt_file(fl, key):
    '''Decrypt a file using cryptography.fernet'''
    f = Fernet(key)
    with open(fl, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)
    with open(fl, "wb") as file:
        file.write(decrypted_data)


""" 
'''This function was made in order to create a master password and cifer it. It only had to be runned once but is important to mention its usage'''
def encrypt_bcrypt(pw):
    '''This action is only neccesary for the proyect purpose, because it is important for the one who tries it to know which one is the cifred password'''
    with open("checking_pass.txt", "w") as file:
        file.write(pw)

    '''Cifering the new password, the gensalt() method is important because the salt works like a key in order to encrypt the password'''
    hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

    '''Converting the cifred password into a string in order to save it on a .txt file'''
    hashed_pw_str = hashed_pw.decode('utf-8')

    '''Saving the cifred password on a .txt file so the program can access it reading the file'''
    with open("password.txt", "w") as file:
        file.write(hashed_pw_str)
"""


def check_pass(pw):
    '''Reading the encoded password on the txt file using bcrypt'''
    with open("password.txt", "r") as file:
        '''Converting it to bytes, according to the library documentaton'''
        stored_pw = file.read().encode('utf-8')

    '''Checking if the password stored matches with the inserted one'''
    if bcrypt.checkpw(pw.encode('utf-8'), stored_pw):
        return True
    return False



def change_pass(old_pw, new_pw):
    '''Changing the existant master password into a new one'''
    if not check_pass(old_pw):
        return False

    '''Cifering the new password'''
    hashed_pw = bcrypt.hashpw(new_pw.encode('utf-8'), bcrypt.gensalt())

    '''Converting the cifred password into a string in order to save it on a txt'''
    hashed_pw_str = hashed_pw.decode('utf-8')

    '''Saving the password so people trying the program can enter the system, but this file saving the uncrypted password shouldn\'t exist'''
    with open("checking_pass.txt", "w") as file:
        file.write(new_pw)

    '''Saving the cifred password on a txt'''
    with open("password.txt", "w") as file:
        file.write(hashed_pw_str)

    return True


def enter_the_system():
    # Checking the master password in order to access the system
    for i in range(1,11):
        pw = input('\nInsert the master password to enter to the system: ')
        if check_pass(pw):
            break
        print(f'Incorrect password, try again. Attempts remaining: {10-i}')
        if i == 10:
            print('\n\nGoing out uf the system because you are not the owner of the account, don\'t do that again\n\n')
            return False
    return True