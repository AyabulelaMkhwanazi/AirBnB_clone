#!/usr/bin/python3
"""
This module contains unittests for 'User' class.
"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Test the User class."""

    def setUp(self):
        """
        Set up the tests.
        """
        self.user = User()

    def tearDown(self):
        """
        Tear down the tests.
        """
        del self.user

    def test_is_instance(self):
        """
        Test if User is an instance of BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        Test if User attributes are correctly set up.
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
