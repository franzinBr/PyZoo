from PyZoo.typesPyZoo.exceptions.typeException import TypeException

class ExtraArgument():

    """
        key: the name of the argument
        value[0]: the accept type of value
        value[1]: the default value of the argument
    """
    ARGUMENTS = {'ALLOW_OUT_SCHEMA': [True, False]}

    def get(self, *args, **kwargs):
        """
            1 or ALLOW_OUT_SCHEMA -> allow items that do not appeal to the schema
        """
        return self.__mapArguments(*args, **kwargs)

    def __mapArguments(self, *args, **kwargs):
        arguments = {}
        start = 0 if kwargs.get('schema', False) else 1
        for index, argument in enumerate(self.ARGUMENTS, start=start):
            try:
                argument_value = kwargs.get(argument) if kwargs.get(argument, False) else args[index]
                if not isinstance(argument_value, type(self.ARGUMENTS[argument][0])):
                    raise TypeException(type(self.ARGUMENTS[argument][0]), argument_value)
                arguments[argument] = argument_value
            except IndexError as e:
                arguments[argument] = self.ARGUMENTS[argument][1]
        return arguments
