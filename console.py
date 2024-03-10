#!/usr/bin/python3
"""
This module contains a class HBNBCommand that contains the entry point
of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
