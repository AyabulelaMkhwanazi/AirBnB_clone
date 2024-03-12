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
import ast
import cmd
import json
import re
import shlex


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
                if len(args) == 0 or key.split('.')[0] == args[0]:
                    print(str(obj))
                    
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
or updating attribute.
        """
        args = line.split(" ", 2)
        if len(args) <= 3:
            if len(args) <= 1:
                print("** class name missing **")
            elif len(args) <= 2:
                print("** instance id missing **")
            else:
                print("** attribute name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name, id, updates_str = args
            key = class_name + "." + id
            if key not in storage.all():
                print("** no instance found **")
            else:
                updates = ast.literal_eval(updates_str)
                for attr, value in updates.items():
                    setattr(storage.all()[key], attr, value)
                storage.all()[key].save()

    def default(self, line):
        """Method called on an input line when the command prefix is not
recognized.
In this case it will be used to handle the <class name>.all(),
<class name>.count(), <class name>.show(<id>) and
<class name>.destroy(<id>),
<class name>.update(<id>, <attribute name>, <attribute value>),
<class name>.update(<id>, <dictionary representation>) syntax.
        """
        if len(line.split(".")) != 2:
            print("** Unknown syntax: {}".format(line))
            return
        class_name, method = line.split(".")
        # check if the class name is valid
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
        # if the method is 'all()', call the 'do_all' method
        elif method == "all()":
            self.do_all(class_name)
        # if the method is 'count()', call the 'do_count' method
        elif method == "count()":
            self.do_count(class_name)
        # if the method starts with 'show(' and ends with ')', it's a 'show'
        # command
        elif method.startswith("show(") and method.endswith(")"):
            id = method[5:-1]  # extracting the id from the method string
            # remove the quotes from the id if they're present
            id = id.strip('"')
            # call da 'do_show' method with the class name and id as arguments
            self.do_show(class_name + " " + id)
        # if method starts with 'destroy(' & ends with ')', it's a 'destroy'
        # command
        elif method.startswith("destroy(") and method.endswith(")"):
            id = method[8:-1]
            id = id.strip('"')  # extract the quotes, like before (if any)
            # call the 'do_destroy' method with the class name and id as args
            self.do_destroy(class_name + " " + id)
            # if the method starts with 'update(' & ends with ')', its an
            # 'update' command
        elif method.startswith("update(") and method.endswith(")"):
            # extract the id from the method string
            id = method[7: -1].split(", ")[0].strip('"')
            # check if the method contains a dictionary or single attribute
            # update
            if "{" in method and "}" in method:
                # use regular expression to extract dictionary from
                # the method string
                dict_repr = re.search("{.*}", method).group()
                updates = ast.literal_eval(dict_repr)
                # call the 'do_update' method with class name,
                # id, attribute name and attribute value as arguments
                self.do_update(class_name + " " + id + " " + str(updates))
            else:
                # extract attribute name and value from the method string
                attr_name = method[7: -1].split(", ")[1].strip('"')
                attr_value = method[7: -1].split(", ")[2].strip('"')
                # create a dictionary for the update
                updates = {attr_name: attr_value}
                # call the 'do_update' method with class name,
                # id, and the updates dictionary as arguments
                self.do_update(class_name + " " + id + " " + str(updates))

    def do_count(self, class_name):
        """Prints the count of instances based on the class name.
        """
        count = 0
        for key in storage.all():
            if key.split('.')[0] == class_name:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
