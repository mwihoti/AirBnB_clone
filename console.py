#!/usr/bin/python3

"""Command interpreter """

import cmd

class HBNBCommand(cmd.Cmd):
    """Console.py"""

    prompt = "(hbnb)"

    def empty_line(self, line):
        """Does nothing on empthy line"""
        return False

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """With ctrl+d Quits command interpreter"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
