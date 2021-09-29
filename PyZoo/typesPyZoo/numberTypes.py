from .base import NumberTypes


class Int(NumberTypes):

    def __init__(self):
        super().__init__()
        self.rules['type'] = int
    
class Float(NumberTypes):

    def __init__(self):
        super().__init__()
        self.rules['type'] = float