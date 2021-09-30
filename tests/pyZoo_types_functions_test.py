import pytest

from PyZoo import PyZoo
from PyZoo.typesPyZoo.numberTypes import Int, Float
from PyZoo.typesPyZoo.textTypes import String
from PyZoo.typesPyZoo.complexTypes import Object, Array

def test_pyzoo_min_function_number_types():

    value = 10
    type_int = PyZoo.INT().MIN(value)
    type_float = PyZoo.FLOAT().MIN(value)

    assert type_int.rules['min'] == value
    assert type_float.rules['min'] == value

    with pytest.raises(AttributeError):
        type_string = PyZoo.STRING().MIN(value)

    with pytest.raises(AttributeError):
        type_array = PyZoo.ARRAY().MIN(value)
    
    with pytest.raises(AttributeError):
        type_object = PyZoo.OBJECT().MIN(value)

def test_pyzoo_max_function_number_types():

    value = 100
    type_int = PyZoo.INT().MAX(value)
    type_float = PyZoo.FLOAT().MAX(value)

    assert type_int.rules['max'] == value
    assert type_float.rules['max'] == value

    with pytest.raises(AttributeError):
        type_string = PyZoo.STRING().MIN(value)

    with pytest.raises(AttributeError):
        type_array = PyZoo.ARRAY().MIN(value)
    
    with pytest.raises(AttributeError):
        type_object = PyZoo.OBJECT().MIN(value)

def test_pyzoo_regex_function_text_types():

    regex = "[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}"
    type_string = PyZoo.STRING().REGEX(regex)

    assert type_string.rules['regex'] == regex

    with pytest.raises(AttributeError):
        type_int = PyZoo.INT().REGEX(regex)
    
    with pytest.raises(AttributeError):
        type_float = PyZoo.float().REGEX(regex)

    with pytest.raises(AttributeError):
        type_array = PyZoo.ARRAY().REGEX(regex)
    
    with pytest.raises(AttributeError):
        type_object = PyZoo.OBJECT().REGEX(regex)


def test_pyzoo_required_function_common_type():

    type_int = PyZoo.INT().REQUIRED()
    type_float = PyZoo.FLOAT().REQUIRED()
    type_string = PyZoo.STRING().REQUIRED()
    type_array = PyZoo.ARRAY().REQUIRED()
    type_object = PyZoo.OBJECT().REQUIRED()

    assert type_int.rules['required'] == True
    assert type_float.rules['required'] == True
    assert type_string.rules['required'] == True
    assert type_array.rules['required'] == True
    assert type_object.rules['required'] == True

def test_pyzoo_equal_function_common_type():

    type_int = PyZoo.INT().EQUALS(1)
    type_float = PyZoo.FLOAT().EQUALS(2.2)
    type_string = PyZoo.STRING().EQUALS('test')
    type_array = PyZoo.ARRAY().EQUALS([])
    type_object = PyZoo.OBJECT().EQUALS({})

    assert type_int.rules['equals'] == 1
    assert type_float.rules['equals'] == 2.2
    assert type_string.rules['equals'] == 'test'
    assert type_array.rules['equals'] == []
    assert type_object.rules['equals'] == {}

def test_pyzoo_not_equal_function_common_type():

    type_int = PyZoo.INT().NOTEQUALS(1)
    type_float = PyZoo.FLOAT().NOTEQUALS(2.2)
    type_string = PyZoo.STRING().NOTEQUALS('test')
    type_array = PyZoo.ARRAY().NOTEQUALS([])
    type_object = PyZoo.OBJECT().NOTEQUALS({})

    assert type_int.rules['notequals'] == 1
    assert type_float.rules['notequals'] == 2.2
    assert type_string.rules['notequals'] == 'test'
    assert type_array.rules['notequals'] == []
    assert type_object.rules['notequals'] == {}

def test_pyzoo_not_equal_and_equal_overwrites():

    type_int = PyZoo.INT().EQUALS(2).NOTEQUALS(5)

    assert type_int.rules['notequals'] == 5
    with pytest.raises(KeyError):
        assert type_int.rules['equals'] == 2
    
    type_int = PyZoo.INT().NOTEQUALS(16).EQUALS(58)

    assert type_int.rules['equals'] == 58
    with pytest.raises(KeyError):
        assert type_int.rules['NOTEQUALS'] == 16