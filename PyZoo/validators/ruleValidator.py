import re


class RuleValidator(object):

    def __init__(self, *args, **kwargs):

        self.RULE_FUNCTIONS = {
            'type': self.typeValidator,
            'equals': self.equalsValidator,
            'notequals': self.notEqualsValidator,
            'required': self.requiredValidator,
            'min': self.minValidator,
            'max': self.maxValidator,
            'regex': self.regexValidator,
        }
    
    def typeValidator(self, value, rule):
        return isinstance(value, rule)
        
    def equalsValidator(self, value, rule):
        return value == rule
    
    def notEqualsValidator(self, value, rule):
        return value != rule
    
    def requiredValidator(self, value, rule):
        return True
    
    def minValidator(self, value, rule):
        return value >= rule
    
    def maxValidator(self, value, rule):
        return value <= rule
    
    def regexValidator(self, value, rule):
        return re.search(regex, str(value)) is not None  