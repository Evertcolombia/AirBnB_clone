#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():

    """
        Prvate class attributes
    """
    __file_path = "file.json"
    __objects = {}

    """
        Public class attributes and methods
    """
    def all(self):
        """
            Return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key obj-classname.id
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
            serializes __objects to th JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            dict_cp = {}

            for key, value in FileStorage.__objects.items():
                dict_cp[key] = value.to_dict()
            f.write(json.dumps(dict_cp))

    def reload(self):
        """
            deserializes the JSON fle to __objects (only if the JSON
            file)
        """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                old_dict = f.read()
                list_dict = json.loads(old_dict)

                for key, value in list_dict.items():
                    x = eval("BaseModel")(**value)
                    self.__objects[key] = x
        except IOError:
           pass
