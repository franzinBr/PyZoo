from PyZoo.typesPyZoo.base import Type
from PyZoo.typesPyZoo.exceptions.constructorException import ConstructorException
from PyZoo.builderCheck.extraArgument import ExtraArgument


class Builder(object):

    def __init__(self, *args, **kwargs):
        self.schema = self.__getSchema(*args, **kwargs)
        self.__checkSchema()
        extraArgument = ExtraArgument()
        self.arguments = extraArgument.get(*args, **kwargs)
        
    def __getSchema(self, *args, **kwargs):
        try:
            schema = kwargs['schema'] if isinstance(kwargs.get('schema', False), dict) else args[0]
            
            if not isinstance(schema, dict):
                raise ConstructorException()
            return schema
        except IndexError as e:
            raise ConstructorException()

    def __checkSchema(self):
        for field in self.schema:
            if not isinstance(self.schema[field], Type):
                raise ConstructorException()