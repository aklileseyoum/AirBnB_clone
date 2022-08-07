#!/usr/bin/python3

class FileStorage:
    __file_path = './dev/file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        fname = FileStorage.__file_path
        storage_d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            storage_d[bm_id] = bm_obj.to_json(saving_file_storage=True)
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(storage_d, f_io)
    def reload(self):
        """
            if file exists, deserializes JSON file to __objects, else nothing
        """
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)
