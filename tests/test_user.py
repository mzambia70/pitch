import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self): #create an instance  of our User class
        self.new_user = User(password = 'banana')

    def test_password_setter(self):    #test case has a value 
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):   #test that our app falses an AttributeEroor whn we try to access the password property
            with self.assertRaises(AttributeError):
                self.new_user.password

        def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('banana'))