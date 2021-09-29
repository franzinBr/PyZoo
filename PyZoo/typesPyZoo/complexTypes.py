from .base import ComplexTypes, Type
from .exceptions.typeException import TypeException
from .exceptions.constructorException import ConstructorException

class Intermediary(ComplexTypes):

    def checkConstruction(self, value):
        if not isinstance(value, Type):
            raise ConstructorException()

    def buildComplexStructure(self, complex):
        if complex:
            for i, field in enumerate(complex):
                cfield = complex[field] if isinstance(complex, dict) else field
                self.checkConstruction(cfield)
                cfield = {field: complex[field]} if isinstance(complex, dict) else {i: cfield}
                self.rules['rulesComplex'].append(cfield)
    
    def checkComplex(self, value):
        sameType = self.checkType(value)
        if 'complex' not in self.rules.keys() or sameType is False: 
            return sameType
    
        
class Object(Intermediary):

    def __init__(self, object = None):
        if object is not None and not isinstance(object, dict):
            raise TypeException(dict, type(object))

        super().__init__(object)
        self.rules['type'] = dict

        self.buildComplexStructure(object)

class Array(Intermediary):

    def __init__(self, array = None):
        if array is not None and not isinstance(array, list):
            raise TypeException(list, type(array))
        
        super().__init__(array)
        self.rules['type'] = list

        self.buildComplexStructure(array)