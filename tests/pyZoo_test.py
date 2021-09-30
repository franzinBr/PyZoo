import pytest

from PyZoo import PyZoo
from PyZoo.validators.exceptions.objectException import ObjectException
from PyZoo.validators.exceptions.argumentException import ArgumentException


@pytest.fixture
def pyzoo_simple_schema(): 
    return PyZoo({
        'foo': PyZoo.STRING().REQUIRED(),
        'bar': PyZoo.INT()
    })

@pytest.fixture
def pyzoo_simple_schema_with_allow_out_schema_active(): 
    return PyZoo({
        'foo': PyZoo.STRING(),
        'bar': PyZoo.INT()
    }, ALLOW_OUT_SCHEMA = True)

@pytest.fixture
def pyzoo_complex_schema(): 
    return PyZoo({
        'id': PyZoo.STRING().REQUIRED(),
        'accountType': PyZoo.INT(),
        'name': PyZoo.STRING().REQUIRED(),
        'address': PyZoo.OBJECT({
            'street': PyZoo.STRING(),
            'number': PyZoo.INT(),
            'coordinates': PyZoo.ARRAY([PyZoo.FLOAT(), PyZoo.FLOAT()])
        })
    })

def test_pyzoo_doesnt_validate_when_object_dosnt_meet_schema_requirements(pyzoo_simple_schema):
    isValid, msgErrors = pyzoo_simple_schema.validate({
        'foo': 5,
        'bar': 'py'
    })

    assert isValid == False
    assert len(msgErrors) == 2

    isValid, msgErrors = pyzoo_simple_schema.validate({
        'bar': 2
    })

    assert isValid == False
    assert len(msgErrors) == 1

def test_pyzoo_validate_when_object_meet_schema_requirements(pyzoo_simple_schema):
    isValid, msgErrors = pyzoo_simple_schema.validate({
        'foo': 'foo',
        'bar': 2
    })

    assert isValid == True
    assert len(msgErrors) == 0

def test_pyzoo_validate_raise_exception_when_allow_out_schema_is_true(pyzoo_simple_schema_with_allow_out_schema_active):
    
    isValid, msgErrors = pyzoo_simple_schema_with_allow_out_schema_active.validate({
            'foo': 'foo',
            'bar': 2,
            'extra': 4,
            'extra2': 'dddd',
            'extraN': '32'
    })
    
    assert isValid == True
    assert len(msgErrors) == 0