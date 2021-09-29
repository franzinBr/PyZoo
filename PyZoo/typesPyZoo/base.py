from abc import ABC, abstractmethod

class Type(ABC):

    def __init__(self):
        self.rules = dict()
    
    def EQUALS(self, value):
        self.rules.pop('notequals', None)
        self.rules['equals'] = value
        return self
    
    def NOTEQUALS(self, value):
        self.rules.pop('equals', None)
        self.rules['notequals'] = value
        return self
    
    def REQUIRED(self):
        self.rules['required'] = True
        return self

class NumberTypes(Type, ABC):
    
    def MIN(self, min):
        self.rules['min'] = min
        return self
    
    def MAX(self, max):
        self.rules['max'] = max
        return self

class TextTypes(Type, ABC):

    def REGEX(self, regex):
        self.rules['regex'] = regex
        return self

class ComplexTypes(Type, ABC):

    def __init__(self, val):
        super().__init__()
        if val is not None:
            #self.rules['complex'] = True
            self.rules['rulesComplex'] = []