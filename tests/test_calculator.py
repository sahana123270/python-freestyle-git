import pytest
 
from app.calculator import add,subtract,multiply,division
 
@pytest.mark.smoke 
def test_add():
    assert add(10,20)==30
 
def test_subtract():
    assert subtract(20,10)==10
 
def test_multiply():
    assert multiply(4,4)==16

@pytest.mark.regression 
def test_division():
    assert division(20,5)==4

@ pytest.mark.regression
def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(10,0)