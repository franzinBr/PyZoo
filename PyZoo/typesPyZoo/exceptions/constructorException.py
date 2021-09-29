class ConstructorException(Exception):
    def __str__(self):
        return 'ConstructorException: syntax error in construction'