#!/usr/bin/python3
"""
This module contains a class HBNBCommand that contains the entry point
of the command interpreter.
"""
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "Place", "State", "City",
                     "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """ECF command to exit the program.
        """
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                new_instance = BaseModel()
            elif line == "User":
                new_instance = User()
            elif line == "Place":
                new_instance = Place()
            elif line == "State":
                new_instance = State()
            elif line == "City":
                new_instance = City()
            elif line == "Amenity":
                new_instance = Amenity()
            elif line == "Review":
                new_instance = Review()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
class name and id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
not on the class name.
        """
        args = line.split()
        if len(args) > 0 and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                print(str(obj))

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
or updating attribute.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                # Remove the double quotes from args[3]
                value = args[3].strip('"')
                setattr(storage.all()[key], args[2], value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
