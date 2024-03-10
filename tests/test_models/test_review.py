#!/usr/bin/python3
"""
This module contains unittests for the class 'Review'.
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up the tests"""
        self.review = Review()

    def tearDown(self):
        """Tear down the tests"""
        del self.review

    def test_attributes(self):
        """Test if Review attributes are correctly set up"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
