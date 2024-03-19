#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
from console import HBNBCommand
from io import StringIO
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from unittest.mock import patch
import os
import sys
import unittest


class TestHBNBCommand(unittest.TestCase):
    """Unittests for the HBNB command interpreter."""

    def test_prompt_string(self):
        """
        Test for the prompt
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_do_quit(self):
        """Test the do_quit method."""
        console = HBNBCommand()
        self.assertTrue(console.do_quit(""))


class TestHBNBCommandWithPatch(unittest.TestCase):
    """Unittests for the HBNB command interpreter with patch."""

    def test_empty_line(self):
        """
        Testing the output of the emptyline method.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd("\n")
            self.assertEqual("", output.getvalue().strip())

    def test_do_EOF(self):
        """Test the do_EOF method."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertTrue(console.do_EOF(""))
            self.assertEqual("\n", output.getvalue())

    def test_do_create(self):
        """Test the do_create method."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("")
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_create("InvalidClass")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_create("BaseModel")
            base_model_id = output.getvalue().strip()
            # UUIDs are 36 characters long
            self.assertEqual(len(base_model_id), 36)

    def test_do_create_user(self):
        """Test the do_create method for User."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("User")
            user_id = output.getvalue().strip()
            # UUIDs are 36 characters long
            self.assertEqual(len(user_id), 36)

    def test_do_create_place(self):
        """Test the do_create method for Place."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("Place")
            place_id = output.getvalue().strip()
            self.assertEqual(len(place_id), 36)

    def test_do_create_state(self):
        """Test the do_create method for State."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("State")
            state_id = output.getvalue().strip()
            self.assertEqual(len(state_id), 36)

    def test_do_create_city(self):
        """Test the do_create method for City."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("City")
            city_id = output.getvalue().strip()
            self.assertEqual(len(city_id), 36)

    def test_do_create_amenity(self):
        """Test the do_create method for Amenity."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("Amenity")
            amenity_id = output.getvalue().strip()
            self.assertEqual(len(amenity_id), 36)

    def test_do_create_review(self):
        """Test the do_create method for Review."""
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            console.do_create("Review")
            review_id = output.getvalue().strip()
            self.assertEqual(len(review_id), 36)

    def test_do_show(self):
        """Test the do_show method."""
        console = HBNBCommand()
        base_model = BaseModel()
        base_model.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("")
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("InvalidClass")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("BaseModel")
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("BaseModel " + "1234")
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("BaseModel " + base_model.id)
            self.assertEqual(str(base_model),
                             output.getvalue().strip())

    def test_do_show_user(self):
        """Test the do_show method for User."""
        console = HBNBCommand()
        user = User()
        user.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("User " + user.id)
            self.assertEqual(str(user), output.getvalue().strip())

    def test_do_show_place(self):
        """Test the do_show method for Place."""
        console = HBNBCommand()
        place = Place()
        place.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("Place " + place.id)
            self.assertEqual(str(place), output.getvalue().strip())

    def test_do_show_state(self):
        """Test the do_show method for State."""
        console = HBNBCommand()
        state = State()
        state.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("State " + state.id)
            self.assertEqual(str(state), output.getvalue().strip())

    def test_do_show_city(self):
        """Test the do_show method for City."""
        console = HBNBCommand()
        city = City()
        city.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("City " + city.id)
            self.assertEqual(str(city), output.getvalue().strip())

    def test_do_show_amenity(self):
        """Test the do_show method for Amenity."""
        console = HBNBCommand()
        amenity = Amenity()
        amenity.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("Amenity " + amenity.id)
            self.assertEqual(str(amenity), output.getvalue().strip())

    def test_do_show_review(self):
        """Test the do_show method for Review."""
        console = HBNBCommand()
        review = Review()
        review.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_show("Review " + review.id)
            self.assertEqual(str(review), output.getvalue().strip())

    def test_do_destroy(self):
        """Test the do_destroy method."""
        console = HBNBCommand()
        base_model = BaseModel()
        base_model.save()

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_destroy("")
            self.assertEqual("** class name missing **", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_destroy("InvalidClass")
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_destroy("BaseModel")
            self.assertEqual("** instance id missing **", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_destroy("BaseModel " + "1234")
            self.assertEqual("** no instance found **", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            console.do_destroy("BaseModel " + base_model.id)
            self.assertEqual("", output.getvalue().strip())
            self.assertNotIn("BaseModel." + base_model.id, storage.all())



if __name__ == '__main__':
    unittest.main()
