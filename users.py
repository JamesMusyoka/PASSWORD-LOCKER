import pyperclip
class Users:
    '''
    Class that generates new instances of a user.
    '''

    user_list = []

    def __init__(self, first_name, last_name, email, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def save_users(self):
        '''
        This method saves Users objects into the user_list.
        '''

        Users.user_list.append(self)

    def delete_users(self):
        '''
        This method deletes a saved users from the user_list.
        '''

        Users.user_list.remove(self)

    @classmethod
    def find_by_email(cls, email):
        '''
        This method takes an email and returns user data that matches the email.
        Args:
            email: email  to search
        Returns:
            users information
        '''

        for users in cls.user_list:
            if users.email == email:
                return users

    @classmethod
    def user_exist(cls,email):
        '''
        This method checks if users exists from list.
        Args:
        email: email to search if it exists.
        Returns:
        True or false depending on if it exists.
        '''

        for users in cls.user_list:
            if users.email == email:
                return True

            return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls, email):
        users_found = Users.find_by_email("jamesmu475@gmail.com")
        pyperclip.copy(users_found.email)
