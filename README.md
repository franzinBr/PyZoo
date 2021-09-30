# PyZoo
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

## Getting Started
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

