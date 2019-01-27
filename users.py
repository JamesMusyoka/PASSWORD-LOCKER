import pyperclip

class User:
    '''
    Class that generates new instances of a user.
    '''

    user_list = []

    def __init__(self, first_name, last_name, email_address, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password


    def save_user(self):
        '''
        This method saves user objects into the user_list.
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        This method deletes a saved user from the user_list.
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_email_address(cls, email_address):
        '''
        This method takes an email and returns user data that matches the email.
        Args:
            email: email address to search
        Returns:
            user information
        '''

        for user in cls.user_list:
            if user.email_address == email_address:
                return user

    @classmethod
    def user_exists(cls,email_address):
        '''
        This method checks if user exists from list.
        Args:
        email: email address to search if it exists.
        Returns:
        True or false depending on if it exists.
        '''

        for user in cls.user_list:
            if user.email_address == email_address:
                return True

            return False

    # @classmethod
    # def copy_email_address(cls, email_address):
    #     user_found = User.find_by_email_address(email_address)
    #     pyperclip.copy(user_found.email_address)
