import unittest
from app import Signup

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.user_1 = Signup('Mac', 'Macgyver','0772190349','', 123)
        self.user_2 = Signup('John', 'Wick','0779202121','', 234)

    def tearDown(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.user_1.fullname, 'Mac Macgyver')
        self.assertEqual(self.user_2.fullname, 'John Wick')

        self.user_1.f_name = 'Chris'
        self.user_2.f_name = 'Tucker'

        self.assertEqual(self.user_1.fullname, 'Chris Macgyver')
        self.assertEqual(self.user_2.fullname, 'Tucker Wick')

    def test_email(self):
        self.assertEqual(self.user_1.email, 'Mac.Macgyver@gmail.com')
        self.assertEqual(self.user_2.email, 'John.Wick@gmail.com')

        self.user_1.f_name = 'Chris'
        self.user_2.f_name = 'Tucker'

        self.assertEqual(self.user_1.email, 'Chris.Macgyver@gmail.com')
        self.assertEqual(self.user_2.email, 'Tucker.Wick@gmail.com')

    def test_password(self):
        pass






