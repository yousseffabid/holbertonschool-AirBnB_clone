#!/usr/bin/env python3
from json import dumps, loads
from os.path import exists


class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        my_json = dumps(self.__objects)
        with open(self.__file_path, 'w') as my_file:
            my_file.write(my_json)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                self.__objects = loads(my_file.read())
