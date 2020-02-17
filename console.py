#!/usr/bin/python3
"""
This is module define the Cmd class for command line in python
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        str = arg.split()
        print(str)
        print(str[0])
        """get the len the split arg"""
        """if the len s less to 1 print clas missing and return"""
        """ if the index 0 of the split line is not in allow class"""             """print clas does not exist and return """
        """ if len of splted line is less 2 pr id missin and retur """
        """get all the instances from the file storage """
        """ get and obje reference using the splited[0] and[1] with a . in the half"""

        """if the object reference is in the nstances.keys()"""
        """print the dict in the intancess passing obj reference a
s key"""
        """else print not instance found """

                

    def help_create(self):
        print("-- Sintax: create class_name")
        print("creat a and save instance for BaseModel")

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
