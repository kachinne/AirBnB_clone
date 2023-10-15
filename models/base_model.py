#!/usr/bin/python3
"""Defining the BaseMofel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
"""This will represent the BaseModel of HBnB projects."""

def __init__(self, *args,**kwargs):
    """Initializing a new BaseModel.

    Args:
    *args (any): Used.
    **kwargs (dict): key/value pairs of attributes.
    """
    tformat = "%Y-%m-%dT%H:%M:%S.%f"
    self.id = str(uuid4())
    self.created_at = datetime.today()
    self-updated_at = datetime.today()
    if len(kwargs) != 0:
        for k, v in kwargs.items():
            self.__dict__[k] = datetime.strptime(v, tformat)
        else:
            self.__dict__[k] = v
        else:
            models.storage.new(self)

def save(self):
    """Time to update the update_at with the current datetime."""
    self.update_at = datetime.today()
    models.storage.save()

def to_dict(self):
    """Such will return the dictionary of the BadeModel instance.

    including the key/value pair __class__ representing
    the class name of the object.
    """
    rdict = self.__dict__.copy()
    rdict["created_at"] = self.created_at.isoformat()
    rdict["updated_at"] = self.updated_at.isoformat()
    rdict["__class__"] = self.__class__.__name__
    return rdict

def __str__(self):
    """This will return the print/str representation of the BaseModel instance."""
    clname = self.__class__.__name__
    return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
