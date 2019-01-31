import unittest
from users import Users
import pyperclip


class TestUsers(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_users = Users("James","Musyoka","jamesmu475@gmail.com","37472377")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_users.first_name,"James")
        self.assertEqual(self.new_users.last_name,"Musyoka")
        self.assertEqual(self.new_users.email,"jamesmu475@gmail.com")
        self.assertEqual(self.new_users.password,"37472377")

    def test_save_users(self):
        """
        test_save_users test case to test if the users object saved into the user_list
        """
        self.new_users.save_users()
        self.assertEqual(len(Users.user_list),1)

    def tearDown(self):
        """
        tearDown method that cleans up after each test has run
        """

        Users.user_list = []

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our users_list
        '''
        self.new_users.save_users()
        test_users = Users("Test","user","password","email")
        test_users.save_users()
        # @classmethod
        self.assertEqual(len(Users.user_list),2)


    def test_delete_users(self):
        '''
        test_delete_users to test if we can remove a users from our user list
        '''
        self.new_users.save_users()
        test_users = Users("Test","user","password","email")
        test_users.save_users()

        self.new_users.delete_users()
        self.assertEqual(len(Users.user_list),1)

    def test_find_users_by_email(self):
        '''
        test to check if we can find a users by account name and display information
        '''

        self.new_users.save_users()
        test_users = Users("Test","user","jamesmu475@gmail.com","password",)
        test_users.save_users()

        found_users = Users.find_by_email("jamesmu475@gmail.com")

        self.assertEqual(found_users.email,test_users.email)

    def test_users_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the users.
            '''

            self.new_users.save_users()
            test_users = Users("Test","user","jamesmu475@gmail.com","37472377")
            test_users.save_users()

            user_exists = Users.user_exist("jamesmu475@gmail.com")

            self.assertTrue(user_exists)
    def test_display_all_users(self):
            '''
            method that returns a list of all users saved
            '''

            self.assertEqual(Users.display_users(),Users.user_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email  from a found contact
        '''

        self.new_users.save_users()
        Users.copy_email("jamesmu475@gmail.com")

        self.assertEqual(self.new_users.email,pyperclip.paste())

if __name__ == '__main__':
     unittest.main()
