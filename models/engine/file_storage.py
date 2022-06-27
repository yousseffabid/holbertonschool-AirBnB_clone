#!/usr/bin/env python3
from json import dumps, loads
from os.path import exists
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        my_json = dict()
        for key, value in self.__objects.items():
            my_json[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            my_file.write(dumps(my_json))

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                my_json = loads(my_file.read())
                for key, value in my_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
