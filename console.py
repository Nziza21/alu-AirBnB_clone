#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[args[0]]()
        storage.new(obj)
        storage.save()
        print(obj.id)

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

        key = args[0] + "." + args[1]
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        print(objs[key])

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

        key = args[0] + "." + args[1]
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        storage.save()

    def do_all(self, arg):
        args = arg.split()
        objs = storage.all()

        if len(args) > 0:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            objs = {
                k: v for k, v in objs.items()
                if k.startswith(args[0] + ".")
            }

        for obj in objs.values():
            print(obj)

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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        obj = objs[key]
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
