#!/usr/bin/python3
"""
This module contains unittests for the class 'Amenity'.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down the tests"""
        del self.amenity

    def test_attributes(self):
        """Test if Amenity attributes are correctly set up"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)


if __name__ == '__main__':
    unittest.main()
