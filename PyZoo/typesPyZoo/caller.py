from .numberTypes import Int, Float 
from .textTypes import String
from .complexTypes import Object, Array

from abc import ABC, abstractmethod

class Caller(ABC):

    @classmethod
    def INT(self):
        return Int()
    
    @classmethod
    def FLOAT(self):
        return Float()

    @classmethod
    def STRING(self):
        return String()

    @classmethod
    def OBJECT(self, object = None):
        return Object(object)
    
    @classmethod
    def ARRAY(self, array = None):
        return Array(array)
    
