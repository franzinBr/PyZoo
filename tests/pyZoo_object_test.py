import pytest

from PyZoo import PyZoo
from PyZoo.validators.exceptions.objectException import ObjectException


@pytest.fixture
def pyzoo_simple_schema(): 
    return PyZoo({
        'foo': PyZoo.STRING(),
        'bar': PyZoo.INT()
    })

def test_pyzoo_object_validation_must_be_a_dict(pyzoo_simple_schema):
    
    with pytest.raises(ObjectException):
        pyzoo_simple_schema.validate(2)
    with pytest.raises(ObjectException):
        pyzoo_simple_schema.validate([])
    with pytest.raises(ObjectException):
        pyzoo_simple_schema.validate(2.5)
    with pytest.raises(ObjectException):
        pyzoo_simple_schema.validate('test')
    
    pyzoo_simple_schema.validate({})