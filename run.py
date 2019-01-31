#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials
import pyperclip

# # user data:
def create_user(fname, lname, email, username, password):
    '''
    This function creates a new account.
    '''
    new_users = Users(fname, lname, email, username, password)
    return new_users

def save_users(users):
    '''
    This function saves an account.
    '''
    users.save_users()

def delete_users(users):
    '''
    This function deletes an account.
    '''
    user.delete_users()

def find_users(email):
    '''
    This function finds a users by their email address.
    '''
    return Users.find_by_email(email)

def check_existing_users(email):
    '''
    This function checks if a user exists with that email and returns a Boolean.
    '''
    return Users.user_exist(email)

def display_users():
    '''
    This function returns all saved users.
    '''
    return Users.display_users()

def user_exists(email):
    '''
    This functions is to check if a user exists.
    '''
    return User.check_existing_user(email)

# credentials:
def create_credentials(account, username, password):
    new_credentials = Credentials(account, username, password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credentials

def test_save_multiple_credentials(credentials):
    credentials.test_save_multiple_credentials

def delete_credentials(credentials):
    credentials.delete_credentials



def main():
    print("HELLO, WELCOME TO PASSWORD-LOCKER. What is your name?")

    user_name = input()
    print("")

    print(f"Hello {user_name}. What would you like to do?")
    print("\n")

    while True:
        print(
            "Use these short codes : cu - create new user data, du - display user data, fu - find user data, ex - exit ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New Users")
            print("-" * 10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Username ...")
            u_name = input()

            print("Email address ...")
            e_address = input()

            print("password ...")
            password = input()

            save_users(create_user(fname,lname,user_name,email, password))
            print('\n')
            print(f"New Users {f_name} {l_name} created")
            print('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users data")
                print('\n')

                for user in display_users():
                    print("{user.first_name} {user.last_name} .....{user.username}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any user data saved yet")
                print('\n')

        elif short_code == 'fu':

            print("Enter the email you want to search for")

            search_email = input()
            if check_existing_user(search_email):
                search_users = find_users(search_email)
                print("{search_user.first_name} {search_users.last_name}")
                print('-' * 20)

                print("Username.......{search_users.username}")
                print("Email address.......{search_users.email}")
            else:
                print("That user data does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
             print("I really didn't get that. Please use the short codes")
             
if __name__ == '__main__':
    main()
