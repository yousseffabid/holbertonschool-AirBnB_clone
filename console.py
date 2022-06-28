#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    intro = '-Welcome to the HBNB CLI Interface-\n'
    prompt = '(hbnb) '
    ruler = "-"

    def do_EOF(self, arg):
        'Exits the HBNB console'
        exit("")

    def do_quit(self, arg):
        'Exits the HBNB console'
        sys.exit("Thanks for using Hbnb Console")

    def emptyline(self):
        pass

    def do_create(self, line):
        'Creates a new instance of BaseModel.'
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return

        elif len(args[0]) >= 1 and args[0] != 'BaseModel':
            print("** class doesn't exist **")
            return

        elif args[0] == 'BaseModel':
            myobj = eval(args[0])()
            myobj.save()
            print(myobj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based \
 on the class name and id"""
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return

        elif len(args) >= 1 and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        elif len(args) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
            return

        elif len(args) == 2:

            storage.reload()
            myobjects = storage.all()

            if myobjects.get(f'{args[0]}.{args[1]}', 0):
                print(myobjects[f'{args[0]}.{args[1]}'])

            else:
                print("** no instance found **")

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id'
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return

        elif len(args) >= 1 and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        elif len(args) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
            return

        elif len(args) == 2:

            storage.reload()
            myobjects = storage.all()

            if myobjects.get(f'{args[0]}.{args[1]}', 0):
                del myobjects[f'{args[0]}.{args[1]}']
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of\
 all instances based or not on the class name. """
        args = line.split(' ')

        if len(args[0]) == 0 or args[0] == 'BaseModel':
            storage.reload()
            myobjects = storage.all()
            list_obj = []
            for value in myobjects.values():
                list_obj.append(str(value))
            print(list_obj)

        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        'Updates an instance based on the class name and id'
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return
        elif len(args) >= 1 and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
            return

        storage.reload()
        myobjects = storage.all()

        if myobjects.get(f'{args[0]}.{args[1]}', 0):
            if len(args) == 2:
                print("** attribute name missing **")
                return

            elif len(args) == 3:
                print("** value missing **")
                return
            setattr(myobjects[f'{args[0]}.{args[1]}'], args[2], args[3])

            myobjects[f'{args[0]}.{args[1]}'].save()

        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
