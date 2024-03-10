#!/usr/bin/python3
from datetime import datetime
from models.base_model import BaseModel
import unittest
import uuid
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case.
        """
        self.my_model = BaseModel()

    def test_init(self):
        """
        Test that id is assigned a UUID and created_at and updated_at
        are datetime instances.
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_id_assigned_uuid(self):
        """
        Test that id is assigned a UUID.
        """
        try:
            uuid_obj = uuid.UUID(self.my_model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")
        self.assertEqual(uuid_obj.hex, self.my_model.id.replace('-', ''))

    def test_unique_id(self):
        """
        Test that each BaseModel has a unique id.
        """
        another_model = BaseModel()
        self.assertNotEqual(self.my_model.id, another_model.id)

    def test_to_dict(self):
        """
        Test that to_dict returns a dictionary representation of the BaseModel
        instance.
        """
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], "BaseModel")

    def test_created_at_updated_at_format(self):
        """
        Test that created_at and updated_at are in ISO format in the output of
        to_dict.
        """
        self.assertEqual(self.my_model.created_at.isoformat(),
                         self.my_model.to_dict()['created_at'])
        self.assertEqual(self.my_model.updated_at.isoformat(),
                         self.my_model.to_dict()['updated_at'])

    def test_init_with_kwargs(self):
        """
        Test that BaseModel can be initialized with keyword arguments.
        """
        id = str(uuid.uuid4())
        created_at = updated_at = datetime.now().isoformat()
        my_model = BaseModel(id=id, created_at=created_at,
                             updated_at=updated_at)
        self.assertEqual(my_model.id, id)
        self.assertEqual(my_model.created_at.isoformat(), created_at)
        self.assertEqual(my_model.updated_at.isoformat(), updated_at)


if __name__ == '__main__':
    unittest.main()
