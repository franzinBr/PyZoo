import json
import os


class LoaderTemplate(object):

    myPath = os.path.dirname(os.path.abspath(__file__))
    
    DEFAULT_MESSAGES_PATH = myPath + "/templates/DefaultMessages.json"
    DEFAULT_VARIABLES_PATH = myPath + "/templates/DefaultVariables.json"

    def load(self):
        with open(self.DEFAULT_MESSAGES_PATH) as jsonFile:
            defaultMessages = json.load(jsonFile)
            jsonFile.close()

        with open(self.DEFAULT_VARIABLES_PATH) as jsonFile:
            defaultVariables = json.load(jsonFile)
            for variable in defaultVariables:
                str_variables = defaultVariables[variable].replace('[', '').replace(']', '').replace(' ', '')
                list_variables = str_variables.split(',')
                defaultVariables[variable] = list_variables
                
            jsonFile.close()

        return defaultMessages, defaultVariables        