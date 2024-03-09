#!/usr/bin/python3

"""Command interpreter """

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


def parse_cmd(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if brackets is None:
            return [k.strip(",") for k in split(arg)]
        else:
            tokenized_list = split(arg[:brackets.span()[0]])
            parsed_list = [k.strip(",") for k in tokenized_list]
            parsed_list.append(brackets.group())
            return parsed_list
    else:
        tokenized_list = split(arg[:braces.span()[0]])
        parsed_list = [k.strip(",") for k in lexer]
        parsed_list.append(braces.group())
        return parsed_list


class HBNBCommand(cmd.Cmd):
    """Console.py"""

    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    
    }
    def default(self, line):
        """
        Defines class default to handle invalid input gracefully by
        attempting to match it against known command patterns.
        """
        lndict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        get_match = re.search(r"\.", line)
        if get_match is not None:
            arg = [line[:get_match.span()[0]], line[get_match.span()[1]:]]
            get_match = re.search(r"\((.*?)\)", line[1])
            if get_match is not None:
                command = [line[1][:get_match.span()[0]], match.group()[1:-1]]
                if command[0] in lndict.keys():
                    call = "{} {}".format(Line[0], command[1])
                    return lndict[command[0]](call)
            print("*** Unknown syntax: {}".format(line))
            return False


    def empty_line(self, line):
        """Does nothing on empthy line"""
        return False

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_create(self, line):
        """create new instance of BaseModel"""
        arg = parse_cmd(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, line):
        """Defines Show : to retrieve an instance based on its ID"""
        arg = parse_cmd(line)
        objinst = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objinst:
            print("** no instance found **")
        else:
            print(objinst["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """Deletes an instance based on id"""
        arg = parse_cmd(line)
        objinst = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objinst.keys():
            print("** no instance found **")
        else:
            del objinst["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        arg = parse_cmd(line)
        if len(arg) > 0 and arg[0]  not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            ob = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    ob.append(obj.__str__())
                elif len(arg) == 0:
                    ob.append(obj.__str__())
            print(ob)

    def do_update(self, line):
        """Updates an instance based on id
        by adding or updating an attribute
        """
        if (self.my_err(line, 4) == 1):
            return
        arg = line.split()
        up = storage.all()
        for i in range(len(arg[1:]) + 1):
            if arg[i][0] == '"':
                arg[i] = arg[i].replace('"', "")
        key = arg[0] + '.' + arg[1]
        attr_1 = args[2]
        attr_2 = args[3]
        try:
            if attr_2.isdigit():
                attr_2 = int(attr_2)
            elif float(attr_2):
                attr_2 = float(attr_2)
        except ValueError:
            pass
        attr = type(up[key]).__dict__
        if attr_1 in attr.keys():
            try:
                attr_2 = type(attr[attr_1])(attr_2)
            except Exception:
                print("You keyed in wrong value type")
                return
        setattr(up[key], attr_1, attr_2)
        storage.save()

    def do_count(self, arg):
        """
        Defines count to retrieve the number of instances of a class:
        """
        args = parse_cmd(arg)
        counts = 0
        for objs in storage.all().values():
            if args[0] == objs.__class__.__.__name__:
                counts += 1
        print(count)

    def do_EOF(self, line):
        """With ctrl+d Quits command interpreter"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
