from PyZoo.formatter.loaderTemplate import LoaderTemplate

from itertools import chain

class Formatter(object):
    
    def __init__(self):
        loaderTemplate = LoaderTemplate()
        self.messages, self.variables = loaderTemplate.load()
    
    def __getName(self, error, namespace):
        if namespace is None:
            return error

        if isinstance(error, int):
            return "{}[{}]".format(namespace, error)
        
        return "{}.{}".format(namespace, error)


    def format(self, errors, namespace=None):
        msg = []
        i = 0
        for error in errors:
            name = self.__getName(error, namespace)
            errors_item = errors[error]

            for error_item in errors_item:
                if any(isinstance(item, list) for item in list(error_item.values())):
                    msg_internal = self.format(error_item, name)
                    msg += msg_internal
                else:
                    error_type = list(error_item.keys())[0]
                    error_infos = {
                        'name': name,
                        'rule': error_item['rule'],
                        'value': error_item['value'],
                    }
                    raw_msg = self.messages[error_type]
                    variables = self.variables[error_type]
                    format_values = [error_infos[value] for value in error_infos if value in variables]
                    msg.append(raw_msg.format(*format_values))
                    
        return msg


                    
                    
                    
