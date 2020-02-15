#!/usr/bin/python3


class FileStorage():

    """
        Prvate class attributes
    """
    __file_path = "path.json" #path to the json file
    __objects = {} # will store all objects by class_name.id

    """
        Public class attributes and methods
    """
    def all(self):
        """
            Return the dictionary __objects
        """
        pass

    def new(self, obj):
        """
            sets in __objects the obj with key obj-classname.id
        """
        pass

    def save(self):
        """
            serializes __objects to th JSON file (path: __file_path)
        """
        dict_cp = __objects.copy()

        for k, v in dict_cp:
            dict_cp[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8')as f:
            f.write(json.dumps(dict_cp))

    def reload(self):
        """
            deserializes the JSON fle to __objects (only if the JSON f            ile (__file_path) exists ; otherwise, do nothing. If the f            ile does not exist, no exception should be raised)
        """
        pass
