#!/usr/bin/python3
"""
This is module define the Cmd class for command line in python
"""

import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
import json


def validate(list_args):
    if list:
        len_list = len(list_args)

        if len_list < 1:
            print("** class name missing **")
            return

        if (list_args[0] != "BaseModel" and
                list_args[0] != "User"):
            print("** class doesn't exist **")
            return

        if len_list < 2:
            print("** instance id missing **")
            return

        obj_reference = list_args[0] + '.' + list_args[1]
        return obj_reference
<<<<<<< HEAD

=======
        
all_classes = ['BaseModel', 'User']
>>>>>>> conole_uptade

class HBNBCommand(cmd.Cmd):
    """
        Class  HBNBCommand
        command line for A&B project
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """ Empty line """
        pass

    def do_quit(self, arg):
        """
            do quit command
        """
        return True

    def do_EOF(self, arg):
        """
            command to end of file
        """
        print("^D")
        return True

    def do_create(self, arg):
        """
            create a new intance of base model and
            saves it in the file.json
        """
<<<<<<< HEAD
        if arg and (arg == "BaseModel" or arg == "User"):
=======
        if arg and arg in all_classes:
>>>>>>> conole_uptade
            cl_name = eval(arg + '()')
            print(cl_name.id)
            print(cl_name)
            cl_name.save()

        elif not arg:
            print("** class name missing **")

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            show an intance if exist when the user type
            the class and id of the instance
        """
        arg_list = arg.split()
        obj_refer = ""

        if validate(arg_list):
            obj_refer = validate(arg_list)
            all_instances = storage.all()

            if obj_refer in all_instances.keys():
                reference = all_instances[obj_refer]
                print(reference)
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """
            destroy a object from a dict wit the instances
            of the data application
        """
        arg_list = arg.split()

        if validate(arg_list):
            obj_refer = validate(arg_list)
            all_instances = storage.all()

<<<<<<< HEAD
            if obj_refer in all_instances.keys():
                del all_instances[obj_refer]
=======
            if obj in all_instances.keys():
                del all_instances[obj]
>>>>>>> conole_uptade
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
            show all the instances in total or the one class
            in specific
        """
        all_instances = storage.all()

<<<<<<< HEAD
        if (len(arg) == 0 or
                arg == "BaseModel" or
                arg == "User"):
=======
        if len(arg) == 0 or arg in all_classes:
>>>>>>> conole_uptade
            list = []

            for key in all_instances:
                if arg == "BaseModel" or arg == "User":
                    if type(storage.all()[key]).__name__ == arg:
                        list.append(str(storage.all()[key]))
                else:
                    list.append(str(storage.all()[key]))
            print(list)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
            update and specific dictionary based n the class name
            and the id reference
        """
        arg_list = arg.split()

        if validate(arg_list):
            obj_refer = validate(arg_list)
            all_instances = storage.all()

            if obj_refer in all_instances.keys():
                obj = all_instances[obj_refer]

                if len(arg_list) < 3:
                    print("** attribute name missing **")
                    return

                elif len(arg_list) < 4:
                    print("** value missing **")
                    return

                elif arg_list[2] != "id" and arg_list[2] != \
                        "created_at" and arg_list[2] != "updated_at":

                    value = arg_list[3].replace('"', "")
                    obj.__dict__[arg_list[2]] = value
                    obj.updated_at = datetime.now()
                    storage.save()
                    print(obj)
                    return
            else:
                print("** no instance found **")
                return

    def help_create(self):
        print("-- Sintax: create class_name")
        print("creat a and save instance for BaseModel")

    def help_show(self):
        print("-- Sintax: show class_name id_instance")
        print("show an nstance from a class with the id")

    def help_destroy(self):
        print("-- Sintax: destroy class_name id_instance")
        print("destroy and instance from a class instances")

    def help_all(self):
        print("-- Sintax: all class_name or all")
        print("show all the instances from a class or total")

    def help_update(self):
        print("-- Sintax: update class_name id_instance attr_name value_name")
        print("Update an instance based on the class_name and id")

    def help_EOF(self):
        """
            help command to  end of file
        """
        print("End of File")

    def help_quit(self):
        """
            help command quit
        """
        print("Quit command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
