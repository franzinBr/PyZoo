class ObjectException(Exception):
    def __str__(self):
        return 'ObjectException: validation object must be an instance of dict'