import csv


class Accounts:
    '''This class contains a serie of attributes and methods realted with the personal information of different accounts of the user.'''
    '''Its main usage is to read the elements from the csv file containing the personal information, and also if the user added or deleted accounts, to write the information on the file in order to save the information'''
    def __init__(self, s,m,u,p):
        '''Initializer or constructor'''
        self.site = s
        self.email = m
        self.username = u
        self.password = p

    '''Setters and Getters'''
    @property
    def site(self):
        return self._site
    @site.setter
    def site(self, s):
        self._site = s

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, m):
        self._email = m

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, u):
        self._username = u

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, p):
        self._password = p


    @classmethod
    def read_accounts(cls, f):
        '''Class method that reads the accounts from the csv file, storing each one on one objects, and appending each object to a list of objects to return it to the main program'''
        accounts = []
        with open(f) as file:
            reader = csv.DictReader(file)
            for r in reader:
                accounts.append(cls(r['site'], r['email'], r['username'], r['password']))

            return accounts

    @classmethod
    def write_accounts(cls, f, object):
        '''This class method is used to write the accounts from the list of objects to the csv file to store them safe after the changes the usermade on them'''
        with open(f, 'w') as file:
            writer = csv.DictWriter(file, fieldnames = ['site','email','username','password'])
            writer.writerow({'site':'site','email':'email','username':'username','password':'password'})
            for w in range(len(object)):
                writer.writerow({'site':object[w].site,'email':object[w].email,'username':object[w].username,'password':object[w].password})


    def filltable(self, lst, l, obj):
        '''This method is applied on the array of objects in order to create the perfect format to use the tabulate module, so the information about the accounts of the user can be perfectly displayed on the terminal'''
        for i in range(l):
            lst.append([i+1, obj[i].site, obj[i].email, obj[i].username, obj[i].password])
        return lst
    
