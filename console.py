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
    __valid_classes = ["BaseModel", "User", "Place", "State", "City",
                       "Amenity", "Review"]

    @staticmethod
    def __parse_method(line):
        # Search for content within curly braces
        curly_b = re.search(r"\{(.*?)\}", line)
        # Search for content within square_b
        square_b = re.search(r"\[(.*?)\]", line)

        # If there's no content in curly braces
        if curly_b is None:
            # If there's also no content in square_b
            if square_b is None:
                # Split the argument string and strip commas
                return [item.strip(",") for item in shlex.split(line)]
            else:
                # Split the argument string up to the square_b
                split_square = shlex.split(line[:square_b.span()[0]])
                # Strip commas and append the content in square_b
                parsed_args = [item.strip(",") for item in split_square]
                parsed_args.append(square_b.group())
                return parsed_args
        else:
            # Split the argument string up to the curly braces
            split_curly = shlex.split(line[:curly_b.span()[0]])
            # Strip commas and append the content in curly braces
            parsed_args = [item.strip(",") for item in split_curly]
            parsed_args.append(curly_b.group())
            return parsed_args

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
and prints the id.
Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
        elif line not in self.__valid_classes:
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
class name and id. Usage: show <class_name> <id> or <class_name>.show(<id>)"""
        args = self.__parse_method(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__valid_classes:
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
    Usage: destroy <class_name> <id> or <class_name>.destroy(<id>)
        """
        args = self.__parse_method(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__valid_classes:
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
    Usage: all or all <class_name> or <class_name>.all()
        """
        args = self.__parse_method(line)
        if len(args) > 0 and args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if len(args) == 0 or key.split('.')[0] == args[0]:
                    print(str(obj))

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
a given attribute key/value pair or dictionary.
    Usage: update <class_name> <id> <attribute_name> <attribute_value> or
    <class_name>.update(<id>, <attribute_name>, <attribute_value>) or
    <class_name>.update(<id>, <dictionary>)
        """
        args = self.__parse_method(line)
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                attr_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = attr_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    attr_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = attr_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def default(self, line):
        """
        Method called on an input line when the command prefix is not
        recognised.
        In this case, it tries to __parse_method the line as a command
        in the format <class>.<command>(<args>).
        """
        # Dictionary of available commands
        command_dictionary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        # Check if the line contains a '.'
        match = re.search(r"\.", line)
        if match is not None:
            # If it does, split the line into the class name and the rest
            class_command = [line[:match.span()[0]],
                             line[match.span()[1]:]]

            # Check if the rest of the line contains a '(' and a ')'
            match = re.search(r"\((.*?)\)", class_command[1])
            if match is not None:
                # If it does, split the rest of the line into the command
                # and the arguments
                command_args = [class_command[1][:match.span()[0]],
                                match.group()[1:-1]]

                # Check if the command is in the dictionary of available
                # commands
                if command_args[0] in command_dictionary.keys():
                    # If it is, format the arguments and call the command
                    format_args = "{} {}".format(class_command[0],
                                                 command_args[1])
                    return command_dictionary[command_args[0]](format_args)

        # If the line couldn't be parsed as a command, print an error message
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_count(self, line):
        """Prints the count of instances based on the class name.
    Usage: count <class_name> or <class_name>.count()
        """
        args = self.__parse_method(line)
        count = 0
        for key in storage.all().values():
            if args[0] == key.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
