#!/usr/bin/python3
"""Defines the HBnB console- command interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if brackets is None:
            return [k.strip(",") for k in split(arg)]
        else:
            token_list = split(arg[:brackets.span()[0]])
            parsed_list = [k.strip(",") for k in token_list]
            parsed_list.append(brackets.group())
            return parsed_list
    else:
        token_list = split(arg[:braces.span()[0]])
        parsed_list = [k.strip(",") for k in token_list]
        parsed_list.append(braces.group())
        return parsed_list


class HBNBCommand(cmd.Cmd):
    """Defines class the HBNBcommand interpreter
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing on empty line."""
        return False

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        command_handlers = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_parts = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_parts[1])
            if match is not None:
                command = [arg_parts[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_handlers.keys():
                    full_command = "{} {}".format(arg_parts[0], command[1])
                    return command_handlers[command[0]](full_command)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, line):
        """exit  program."""
        return True

    def do_EOF(self, line):
        """ctrl + D exit the program."""
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        """
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            print("** class name missing **")
        elif arg_parts[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_parts[0])().id)
            storage.save()

    def do_show(self, line):
        """
        Display the string representation of a class instance of a given id.
        """
        line_parts = parse(line)
        store = storage.all()
        if len(line_parts) == 0:
            print("** class name missing **")
        elif line_parts[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_parts) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line_parts[0], line_parts[1]) not in store:
            print("** no instance found **")
        else:
            print(store["{}.{}".format(line_parts[0], line_parts[1])])

    def do_destroy(self, line):
        """
        Delete a class instance of a given id.
        """
        line_parts = parse(line)
        store = storage.all()
        if len(line_parts) == 0:
            print("** class name missing **")
        elif line_parts[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line_parts) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line_parts[0], line_parts[1]) not in store.keys():
            print("** no instance found **")
        else:
            del store["{}.{}".format(line_parts[0], line_parts[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display string representations of all instances of a given class.
        """
        arg_parts = parse(arg)
        if len(arg_parts) > 0 and arg_parts[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_array = []
            for obj in storage.all().values():
                if len(arg_parts) > 0 and arg_parts[0] ==
                obj.__class__.__name__:
                    obj_array.append(obj.__str__())
                elif len(arg_parts) == 0:
                    obj_array.append(obj.__str__())
            print(obj_array)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.
        """
        arg_parts = parse(arg)
        counts = 0
        for obj in storage.all().values():
            if arg_parts[0] == obj.__class__.__name__:
                counts += 1
        print(counts)

    def do_update(self, arg):
        """
        Update a class instance of a given id by adding or updating
        a given attribute  dictionary.
        """
        arg_parts = parse(arg)
        store = storage.all()

        if len(arg_parts) == 0:
            print("** class name missing **")
            return False
        if arg_parts[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_parts) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_parts[0], arg_parts[1]) not in store.keys():
            print("** no instance found **")
            return False
        if len(arg_parts) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_parts) == 3:
            try:
                type(eval(arg_parts[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_parts) == 4:
            objects = store["{}.{}".format(arg_parts[0], arg_parts[1])]
            if arg_parts[2] in objects.__class__.__dict__.keys():
                valtype = type(objects.__class__.__dict__[arg_parts[2]])
                objects.__dict__[arg_parts[2]] = valtype(arg_parts[3])
            else:
                objects.__dict__[arg_parts[2]] = arg_parts[3]
        elif type(eval(arg_parts[2])) == dict:
            objects = store["{}.{}".format(arg_parts[0], arg_parts[1])]
            for m, n in eval(arg_parts[2]).items():
                if (m in objects.__class__.__dict__.keys() and
                        type(objects.__class__.__dict__[m]) in
                        {str, int, float}):
                    valtype = type(objects.__class__.__dict__[m])
                    objects.__dict__[m] = valtype(n)
                else:
                    objects.__dict__[m] = n
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
