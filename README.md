# PyZoo

[![pypi](https://img.shields.io/pypi/v/pyzoo.svg)](https://pypi.org/project/PyZoo/)

Python library for data validation


### Requirements
- Python >= 3

## ⚙ Installation (PyPi)
```
pip install PyZoo
```
## ⚙ Installation (Last Version/manually)
To download the latest development version of PyZoo:
```
git clone https://github.com/franzinBr/PyZoo.git
cd PyZoo
```
install and run test
```
sudo python3 setup.py install
sudo python3 setup.py pytest
```

## 🏁 Getting Started
to import the module
```python
from PyZoo import PyZoo 
```
PyZoo has the following types of data:
```python
from PyZoo import PyZoo

# Number Types
PyZoo.INT() # -4,-3,523, 0, 49...
PyZoo.FLOAT() # 3.21, -93, 4.9...

# Text Types
PyZoo.STRING() # 'python', "test", "pyzoo", "name"....

# Complex Types
PyZoo.OBJECT() # {}, {'name': "foo", "age": 19}...
PyZoo.ARRAY() # [], [0,1,2], [23.2], ['hello', 53]...
```

for data validation it is necessary to build a schema, an object that will define the expected data format and its rules
```python
schema = PyZoo({
    'name': PyZoo.STRING(),
    'email': PyZoo.STRING(),
    'weight': PyZoo.FLOAT()
}, ALLOW_OUT_SCHEMA=True)
```
with this scheme we define that we will validate 3 data: name (string), email (string) and weight(float)
if you looked at the constructor carefully, you noticed that there is a flag called `ALLOW_OUT_SCHEMA` this flag defines whether fields that are not defined in the schema are allowed

by default its value is false, that is, if we pass data whose name is different from 'name', 'email' and 'weight' an error will be generated
in this case, as we set to true, validation ignores data with names that are not in the schema

With that in mind, to validate the data using this schema, we just do the following:
```python
 isValid, msgErrors = schema.validate({
    'name': 'pyzoo',
    'email': 'test@pyzoo.com',
    'weight': 0.04
 })
```
the `validate` function returns 2 items, the first being a boolean that defines whether the object is valid or not
and the second is an array containing all error messages if the object is not valid


## 🔧 FUNCTIONS
in addition to validations by type, there are other functions that define new validation rules

| function  | type   | definition                                                                  | example                                          |
|-----------|--------|-----------------------------------------------------------------------------|--------------------------------------------------|
| REQUIRED  | All    | the field is now required to become valid                                   | PyZoo.STRING().REQUIRED()                        |
| MIN       | Number | to be valid, the field must be greater  than or equal to the minimum value. | PyZoo.INT().MIN(2)                               |
| MAX       | Number | to be valid, the field must be less  than or equal to the minimum value.    | PyZoo.FLOAT().MAX(100)                           |
| EQUALS    | All    | to be valid the field must be the same (this function overwrites notequal)  | PyZoo.STRING().EQUALS('pyzoo')                   |
| NOTEQUALS | All    | to be valid the field must not be the same (this function overwrites equal) | PyZoo.ARRAY().NOTEQUALS([])                      |
| REGEX     | Text   | to be valid the field must follow the regex  pattern                        | PyZoo.STRING().REGEX("[A-Z]{1,2}[0-9][A-Z0-9]?") |

