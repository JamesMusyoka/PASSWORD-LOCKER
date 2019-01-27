import string
import random

class Credentials:
    '''
    Class that generates new instances of credentials.
    '''

    credentials_list = []

    def __init__(self, account, username, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        This methods save credential objects into the credentials_list.
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        This method deletes saved credentials from the credentials_list.
        '''

        Credentials.credentials_list.remove(self)

    def password_generator(self, size=8, chars=string.ascii_letters + string.digits):
        '''
        This method generates a password by returning a string of random characters.
        '''
        return ''.join(random.choice(chars) for i in range(size))
