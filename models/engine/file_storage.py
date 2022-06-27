#!/usr/bin/env python3
from json import dumps, loads


class FileStorage:
    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.name}"] = obj

    def save(self):
        my_json = dumps(self.__dict__)
        with open(self.__file_path) as my_file:
            my_file.write(my_json)

    def reload(self):
        with open(self.__file_path) as my_file:
            self.__objects = loads(my_file.read())
