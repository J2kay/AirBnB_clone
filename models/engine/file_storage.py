#!/usr/bin/python3
"""Contains File storing the projects data"""

import json
import os
import datetime


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in object the the key and value"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """Serializes object to a json file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, file)

    def reload(self):
        """Deserializes a json file to python object"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            dict_object = json.load(file)
            dict_object = {
                k: self.classes()[v["__class__"]](**v) for k, v in dict_object.items()
            }
            FileStorage.__objects = dict_object
