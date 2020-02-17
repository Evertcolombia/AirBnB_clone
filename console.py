#!/usr/bin/python3
"""
This is module define the Cmd class for command line in python
"""

import cmd
from models.base_model import BaseModel
from models import storage

def validate(list_args):
    if list:
        len_list = len(list_args)

        if len_list < 1:
            print("** class name missing **")
            return 

        if list_args[0] != "BaseModel":
            print("** class doesn't exist **")
            return 

        if len_list < 2:
            print("** instance id missing **")
            return
        return 1
        

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
        if arg and  arg == "BaseModel":
            cl_name = eval(arg + '()')
            print(cl_name.id)
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

        if validate(arg_list) == 1:
            obj = arg_list[0] + '.' + arg_list[1]
            all_instances = storage.all()       

            if obj  in all_instances.keys():
                reference = all_instances[obj]
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

        if validate(arg_list) == 1:
            obj = arg_list[0] + '.' + arg_list[1]
            all_instances = storage.all()

            if obj in all_instances.keys():
                del all_instances[obj]
                print("deleted")
                storage.save()
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
