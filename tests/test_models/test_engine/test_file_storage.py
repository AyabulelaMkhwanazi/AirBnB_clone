#!/usr/bin/python3
"""
This module contains unittests for the class 'FileStorage'.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Test the FileStorage class
    """

    def setUp(self):
        """
        Set up the test case
        """
        self.storage = FileStorage()

    def test_all(self):
        """
        Test that all returns the dictionary __objects.
        """
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new(self):
        """
        Test that new adds an object to __objects.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        key = my_model.__class__.__name__ + "." + my_model.id
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """
        Test that save writes to the JSON file and that reload reads from the
        JSON file.
        """
        my_model = BaseModel()
        my_model.my_number = 89
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        key = my_model.__class__.__name__ + "." + my_model.id
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].my_number, 89)


if __name__ == '__main__':
    unittest.main()
