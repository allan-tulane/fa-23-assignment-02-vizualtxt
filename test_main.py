from main.py import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2
    assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(10)).decimal_val == 100
    assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(20)).decimal_val == 20*20
