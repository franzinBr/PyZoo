from .base import TextTypes


class String(TextTypes):

    def __init__(self):
        super().__init__()
        self.rules['type'] = str
