from PyZoo.typesPyZoo.caller import Caller
from PyZoo.builderCheck.builderCheck import Builder
from PyZoo.validators.validator import Validator 

class PyZoo(Caller, Builder, Validator): 
    
    def __init__(self, *args, **kwargs):
        Builder.__init__(self, *args, **kwargs)
        Validator.__init__(self)
    
