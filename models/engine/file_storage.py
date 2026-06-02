import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        with open(self.__file_path, "r") as f:
            data = json.load(f)

        for key, value in data.items():
            cls_name = value["__class__"]
            if cls_name in classes:
                self.__objects[key] = classes[cls_name](**value)
