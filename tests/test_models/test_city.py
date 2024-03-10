#!/usr/bin/python3
"""
This module contains unittests for the class 'City'.
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up the tests"""
        self.city = City()

    def tearDown(self):
        """Tear down the tests"""
        del self.city

    def test_attributes(self):
        """Test if City attributes are correctly set up"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)


if __name__ == '__main__':
    unittest.main()
