#!/usr/bin/python3
"""FileStorage class"""

import json


class FileStorage:
    """Serializes and deserializes objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_dict = {}

        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        try:
            from models.base_model import BaseModel
            from models.user import User

            classes = {
                "BaseModel": BaseModel,
                "User": User
            }

            with open(self.__file_path, "r") as f:
                data = json.load(f)

            for key, value in data.items():
                cls_name = value["__class__"]
                if cls_name in classes:
                    self.__objects[key] = classes[cls_name](**value)

        except FileNotFoundError:
            pass
