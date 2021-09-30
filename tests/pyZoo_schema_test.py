import pytest

from PyZoo import PyZoo
from PyZoo.typesPyZoo.exceptions.constructorException import ConstructorException 

def test_pyzo_schema_builder_fail_when_is_empty():
    with pytest.raises(ConstructorException):
        PyZoo()

def test_pyzo_schema_builder_fail_when_first_argument_isnt_dict():
    with pytest.raises(ConstructorException):
        PyZoo(2)
    
    with pytest.raises(ConstructorException):
        PyZoo('test')
    
    with pytest.raises(ConstructorException):
        PyZoo([])
    
    with pytest.raises(ConstructorException):
        PyZoo(())
    
    with pytest.raises(ConstructorException):
        PyZoo(5.3)
    
    with pytest.raises(ConstructorException):
        PyZoo(True)
    
    with pytest.raises(ConstructorException):
        PyZoo(u'test')

def test_pyzo_schema_builder_success_when_first_argument_is_dict():
    validator = PyZoo({})

    assert validator.schema == {}

def test_pyzo_schema_can_be_kwargs():
    validator = PyZoo(schema={})

    assert validator.schema == {}

def test_pyzo_schema_build_fail_when_kwarg_schema_isnt_dict():
    with pytest.raises(ConstructorException):
        PyZoo(schema=2)
    
    with pytest.raises(ConstructorException):
        PyZoo(schema='test')
    
    with pytest.raises(ConstructorException):
        PyZoo(schema=[])
    
    with pytest.raises(ConstructorException):
        PyZoo(schema=())
    
    with pytest.raises(ConstructorException):
        PyZoo(schema=5.3)
    
    with pytest.raises(ConstructorException):
        PyZoo(schema=True)
    
    with pytest.raises(ConstructorException):
        PyZoo(schema=u'test')