#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""


from uuid import uuid4
from datetime import datetime



class BaseModel:
    """
        attributes and functions for BaseModel class
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = created_at

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_json(self, saving_file_storage=False):
        """
            returns json representation of self
        """
        obj_class = self.__class__.__name__
        bm_dict = {
            k: v if self.__is_serializable(v) else str(v)
            for k, v in self.__dict__.items()
        }
        bm_dict.pop('_sa_instance_state', None)
        bm_dict.update({
            '__class__': obj_class
            })
        if not saving_file_storage and obj_class == 'User':
            bm_dict.pop('password', None)
        return(bm_dict)

    def __str__(self):
        return "[{}] ({}) ({})".format(type(self).__name__, self.id, self.__dict__)

