import pytest

from PyZoo import PyZoo
from PyZoo.typesPyZoo.exceptions.constructorException import ConstructorException
from PyZoo.typesPyZoo.exceptions.typeException import TypeException 


def test_pyzo_first_argument_is_set_as_the_second_constructor_value():
    value = True
    validator = PyZoo({}, value)

    arguments_list = list(validator.arguments.values())

    assert arguments_list[0] == value

    secondValue = False
    validator = PyZoo({}, secondValue)

    arguments_list = list(validator.arguments.values())

    assert arguments_list[0] == secondValue

def test_pyzo_first_argument_is_called_ALLOW_OUT_SCHEMA():
    validator = PyZoo({}, True)

    arguments_names = list(validator.arguments.keys())

    assert arguments_names[0] == 'ALLOW_OUT_SCHEMA'

def test_pyzo_first_argument_must_be_bool():
    with pytest.raises(TypeException):
        PyZoo({}, 5)
    
    with pytest.raises(TypeException):
        PyZoo({}, 's')
    
    with pytest.raises(TypeException):
        PyZoo({}, 5.5)
    
    with pytest.raises(TypeException):
        PyZoo({}, {})
    
    with pytest.raises(TypeException):
        PyZoo({}, [])

    PyZoo({}, True)

    
def test_pyzo_first_argument_is_default_false():
    validator = PyZoo({})

    assert validator.arguments['ALLOW_OUT_SCHEMA'] == False

def test_pyzo_first_argument_can_be_kwargs():
    validator = PyZoo({}, ALLOW_OUT_SCHEMA=True)
    arguments_list = list(validator.arguments.values())

    assert arguments_list[0] == True
    assert validator.arguments['ALLOW_OUT_SCHEMA'] == True

    validator = PyZoo({}, ALLOW_OUT_SCHEMA=False)
    arguments_list = list(validator.arguments.values())

    assert arguments_list[0] == False
    assert validator.arguments['ALLOW_OUT_SCHEMA'] == False

    validator = PyZoo({}, ALLOW_OUT_SCHEMA=False)
    arguments_list = list(validator.arguments.values())

    assert arguments_list[0] == False
    assert validator.arguments['ALLOW_OUT_SCHEMA'] == False