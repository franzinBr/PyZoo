import pytest

from PyZoo import PyZoo
from PyZoo.typesPyZoo.numberTypes import Int, Float
from PyZoo.typesPyZoo.textTypes import String
from PyZoo.typesPyZoo.complexTypes import Object, Array
from PyZoo.typesPyZoo.exceptions.typeException import TypeException
from PyZoo.typesPyZoo.exceptions.constructorException import ConstructorException

def test_pyzoo_int_type():

    type = PyZoo.INT()

    assert isinstance(type, Int)
    assert isinstance(1, type.rules['type'])

def test_pyzoo_float_type():

    type = PyZoo.FLOAT()
    
    assert isinstance(type, Float)
    assert isinstance(3.2, type.rules['type'])

def test_pyzoo_string_type():

    type = PyZoo.STRING()
    
    assert isinstance(type, String)
    assert isinstance('test', type.rules['type'])

def test_pyzoo_array_type():

    type = PyZoo.ARRAY()
    
    assert isinstance(type, Array)
    assert isinstance([], type.rules['type'])

def test_pyzoo_object_type():

    type = PyZoo.OBJECT()
    
    assert isinstance(type, Object)
    assert isinstance({}, type.rules['type'])

def test_pyzoo_array_type_accept_more_itens():

    type_array = PyZoo.ARRAY([PyZoo.INT(), PyZoo.FLOAT()])

    assert isinstance(type_array.rules['rulesComplex'][0][0], Int)
    assert isinstance(1, type_array.rules['rulesComplex'][0][0].rules['type'])
    assert isinstance(type_array.rules['rulesComplex'][1][1], Float)
    assert isinstance(2.7, type_array.rules['rulesComplex'][1][1].rules['type'])

def test_pyzoo_array_type_just_accept_array():

    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY(2)
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY({})
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY('')    
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY(3.24)
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY(u'ss')
    
    type_array = PyZoo.ARRAY([])

def test_pyzoo_array_type_just_accept_pyzoo_types_inside_array():

    with pytest.raises(ConstructorException):
        type_array = PyZoo.ARRAY([2, 'python', 56.3, {}, 23])
    
    type_array = PyZoo.ARRAY([PyZoo.STRING()])

def test_pyzoo_object_type_accept_more_itens():

    type_object = PyZoo.OBJECT({
        'name': PyZoo.STRING().REQUIRED(),
        'lastname': PyZoo.STRING(),
        'age': PyZoo.INT().MIN(18)
    })

    assert isinstance(type_object.rules['rulesComplex'][0]['name'], String)
    assert isinstance(type_object.rules['rulesComplex'][1]['lastname'], String)
    assert isinstance(type_object.rules['rulesComplex'][2]['age'], Int)

    assert type_object.rules['rulesComplex'][0]['name'].rules['required'] == True
    assert type_object.rules['rulesComplex'][2]['age'].rules['min'] == 18


def test_pyzoo_object_type_just_accept_object():

    with pytest.raises(TypeException):
        type_object = PyZoo.OBJECT(2)
    with pytest.raises(TypeException):
        type_object = PyZoo.OBJECT('')    
    with pytest.raises(TypeException):
        type_object = PyZoo.OBJECT(3.24)
    with pytest.raises(TypeException):
        type_object = PyZoo.OBJECT(u'ss')
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY({'2'})
    
    type_object = PyZoo.OBJECT({})

def test_pyzoo_object_type_just_accept_pyzoo_types_inside_object():

    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY({
            'name': 2,
            'id': '332'
        })
    
    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY({
            'name': PyZoo.STRING(),
            'id': '332'
        })

    with pytest.raises(TypeException):
        type_array = PyZoo.ARRAY({
            'foo': PyZoo.ARRAY(2),
        })
    
