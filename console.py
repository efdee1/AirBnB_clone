#!/usr/bin/python3
"""
This is the command line interface for HBNB
    methods:
        do_greet() - Welcomes user to console
        do_create() - Creates a new instance of BaseModel
        do_show() - Prints the string repr of an instance
        do_destroy() - Deletes an instance
        do_all() - Prints all string repr of all instances
        do_udate() - Updates an instance
        do_EOF() - Quit command to exit the CLI
        do_quit() - Quit command to exit the CLI
"""

import cmd, sys, shlex, models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

hbnb_models = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """
    This is the command processor for hbnb console
    """
    prompt = '(hbnb) '

    def do_greet(self, line):
        """
        Welcomes user to console
        """
        print('Welcome to HBNB command line interface')

    def do_create(self, *args):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        if args[0] == '':
            print("** class name missing **")
        elif args[0] in hbnb_models:
            new_instance = hbnb_models[args[0]]()
            print(new_instance.id)
            new_instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in hbnb_models:
            print("** class doesn't exist **")
            return False
        if len(args) <= 1:
            print("** instance id missing **")
            return False
        else:
            inst_key = args[0] + "." + args[1]
            if inst_key in models.storage.all():
                inst_str = models.storage.all()[inst_key]
                print(inst_str)
            else:
                print("** no instance found **")
                return False

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in hbnb_models:
            print("** class doesn't exist **")
            return False
        if len(args) <= 1:
            print("** instance id missing **")
            return False
        else:
            inst_key = args[0] + "." + args[1]
            if inst_key in models.storage.all():
                del models.storage.all()[inst_key]
                models.storage.save()
            else:
                print("** no instance found **")
                return False

    def do_all(self, arg):
        """
        Prints all string representation of all instances 
        based or not on the class name
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) >= 1:
            if args[0] not in hbnb_models:
                print("** class doesn't exist **")
                return False
            else:
                for k in models.storage.all():
                    if args[0] in k:
                        obj_list.append(str(models.storage.all()[k]))
                        print("[" + ", ".join(obj_list) + "]", end="\n")
        else:
            for v in models.storage.all().values():
                obj_list.append(str(v))
            print("[" + ", ".join(obj_list) + "]", end="\n")

    def do_update(self, arg):
        """
        Updates an instance based on the class name 
        and id by adding or updating attribute
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in hbnb_models:
            print("** class doesn't exist **")
            return False
        if len(args) <= 1:
            print("** instance id missing **")
            return False
        else:
            inst_key = args[0] + "." + args[1]
            if inst_key not in models.storage.all():
                print("** no instance found **")
                return False
        if len(args) <= 2:
            print("** attribute name missing **")
            return False
        if len(args) <= 3:
            print("** value missing **")
            return False
        else:
            k = args[0] + "." + args[1]
            setattr(models.storage.all()[k], args[2], args[3])
            models.storage.all()[k].save()
    
    def do_EOF(self, line):
        """
        Quit command to exit the CLI
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the CLI
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()