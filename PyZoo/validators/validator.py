from PyZoo.validators.exceptions.objectException import ObjectException
from PyZoo.validators.argumentRules import ArgumentRules
from PyZoo.validators.ruleValidator import RuleValidator
from PyZoo.validators.utils.listSecure import ListSecure
from PyZoo.formatter.format import Formatter

class Validator(object):
    
    def __init__(self):
        self.errors = {}
    
    def validate(self, *args, **kwargs):
        self.object = self.__getObject(*args, **kwargs)
        self.__checkObject()
        ruleValidator = RuleValidator()
        self.errors = self.__loopValidation(ruleValidator, self.schema, self.object, 1)

        formatter = Formatter()
        msg_errors = formatter.format(self.errors)

        return len(self.errors) == 0, msg_errors


    def __loopValidation(self, ruleValidator, schema, object, n, reference=None):
        ruleErrorsGroup = {}  
        for ruleName in schema:
            if n > 1:
                rules = list(ruleName.values())[0].rules
                ruleName = list(ruleName.keys())[0]
            else:
                rules = schema[ruleName].rules
            
            try:
                value = object.get(ruleName, None)
            except AttributeError:
                value = ListSecure(object).get(ruleName)
            
            ruleErrors = []
            internal = []

            if value is None:
                if 'required' in rules.keys():
                    ruleErrorsGroup[ruleName] = [{'required': False, 'rule': 'required', 'value': None}]
                continue
            
            for rule in rules:
                if rule == 'rulesComplex':
                    if isinstance(value, list) or isinstance(value, dict):
                        internal = self.__loopValidation(ruleValidator, rules['rulesComplex'], value, n+1, ruleName)
                        if internal:
                            ruleErrors.append(internal)   
                else:
                    result = ruleValidator.RULE_FUNCTIONS.get(rule, lambda x,y: 'Invalid')(value, rules[rule])
                    if not result:
                        ruleErrors.append({rule: result, 'rule': rules[rule], 'value': value })
        
            if ruleErrors:
                ruleErrorsGroup[ruleName] = ruleErrors
             
        return ruleErrorsGroup
        
    def __checkObject(self):
        if not isinstance(self.object, dict):
            raise ObjectException()

        argumentRules = ArgumentRules()
        for argument in self.arguments:
            argumentRules.ARGUMENT_RULES[argument](self)
        
        
    def __getObject(self, *args, **kwargs):
        try:
            return kwargs['object'] if kwargs else args[0]
        except IndexError:
            raise ObjectException()