class TypeException(Exception):
    def __init__(self, *args):
        if args:
            self.expected = args[0]
            self.received = args[1]

    def __str__(self):
        if self.expected and self.received:
            return 'TypeException: expected {}, but received {} '.format(self.expected, self.received)

        return 'TypeException has been raised'