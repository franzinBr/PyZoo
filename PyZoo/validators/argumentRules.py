from PyZoo.validators.exceptions.argumentException import ArgumentException

class ArgumentRules(object):

    def __init__(self):

        self.ARGUMENT_RULES = {
            'ALLOW_OUT_SCHEMA': self.allowOutSchema
        }
    
    def allowOutSchema(self, secondSelf):
        ruleActive = secondSelf.arguments.get('ALLOW_OUT_SCHEMA', False)
        for field in list(secondSelf.object):
            if field not in secondSelf.schema.keys():
                if not ruleActive:
                    raise ArgumentException('{} is not in the validation scheme'.format(field))
                secondSelf.object.pop(field)