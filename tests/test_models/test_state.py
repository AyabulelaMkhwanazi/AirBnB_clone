#!/usr/bin/python3
"""
This module contains unittests for the class 'State'.
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up the tests"""
        self.state = State()

    def tearDown(self):
        """Tear down the tests"""
        del self.state

    def test_attributes(self):
        """Test if State attributes are correctly set up"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
