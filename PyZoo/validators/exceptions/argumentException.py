class ArgumentException(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args[0]

    def __str__(self):
        if self.msg:
            return 'ArgumentException: {}'.format(self.msg)

        return 'ArgumentException has been raised'