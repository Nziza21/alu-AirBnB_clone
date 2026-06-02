#!/usr/bin/python3
"""AirBnB console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


classes = {
    "BaseModel": BaseModel,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    # ---------------- CREATE ----------------
    def do_create(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[args[0]]()
        obj.save()
        print(obj.id)

    # ---------------- SHOW ----------------
    def do_show(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    # ---------------- DESTROY ----------------
    def do_destroy(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    # ---------------- ALL ----------------
    def do_all(self, arg):
        args = arg.split()
        objects = storage.all()

        result = []

        if len(args) == 0:
            for obj in objects.values():
                result.append(str(obj))
            print(result)
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        for obj in objects.values():
            if obj.__class__.__name__ == args[0]:
                result.append(str(obj))

        print(result)

    # ---------------- UPDATE ----------------
    def do_update(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr = args[2]
        value = args[3].strip('"')

        if hasattr(obj, attr):
            old_type = type(getattr(obj, attr))
            try:
                value = old_type(value)
            except:
                pass

        setattr(obj, attr, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
