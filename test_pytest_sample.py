import pytest
import sample

# Add tests for valid addition
def test_add_valid_integers():
    checker = sample.Operation()
    result = checker.add(10, 20)
    assert result == 30

def test_add_valid_floats():
    checker = sample.Operation()
    result = checker.add(10.5, 20.5)
    assert result == 31.0

def test_add_valid_mixed():
    checker = sample.Operation()
    result = checker.add(10, 20.5)
    assert result == 30.5

# Add tests for invalid types in addition
def test_add_invalid_string_int():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add('Ram', 10)

def test_add_invalid_string_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add('Ram', False)

def test_add_invalid_string_float():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add('Ram', 10.2)

def test_add_invalid_int_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add(True, 10.2)

def test_add_invalid_float_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add(False, 10.2)

def test_add_invalid_bools():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.add(False, True)

# Add tests for valid subtraction
def test_minus_valid_integers():
    checker = sample.Operation()
    result = checker.minus(20, 10)
    assert result == 10

def test_minus_valid_floats():
    checker = sample.Operation()
    result = checker.minus(20.5, 10.5)
    assert result == 10.0

def test_minus_valid_mixed():
    checker = sample.Operation()
    result = checker.minus(20, 10.5)
    assert result == 9.5

# Add tests for invalid types in subtraction
def test_minus_invalid_string_int():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus('Ram', 10)

def test_minus_invalid_string_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus('Ram', False)

def test_minus_invalid_string_float():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus('Ram', 10.2)

def test_minus_invalid_int_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus(True, 10.2)

def test_minus_invalid_float_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus(False, 10.2)

def test_minus_invalid_bools():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.minus(False, True)

# Add tests for valid multiplication
def test_mul_valid_integers():
    checker = sample.Operation()
    result = checker.mul(10, 20)
    assert result == 200

def test_mul_valid_floats():
    checker = sample.Operation()
    result = checker.mul(10.5, 20.0)
    assert result == 210.0

def test_mul_valid_mixed():
    checker = sample.Operation()
    result = checker.mul(10, 20.5)
    assert result == 205.0

# Add tests for invalid types in multiplication
def test_mul_invalid_string_int():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul('Ram', 10)

def test_mul_invalid_string_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul('Ram', False)

def test_mul_invalid_string_float():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul('Ram', 10.2)

def test_mul_invalid_int_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul(True, 10.2)

def test_mul_invalid_float_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul(False, 10.2)

def test_mul_invalid_bools():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.mul(False, True)

# Add tests for valid division
def test_div_valid_integers():
    checker = sample.Operation()
    result = checker.div(20, 10)
    assert result == 2

def test_div_valid_floats():
    checker = sample.Operation()
    result = checker.div(20.5, 10.0)
    assert result == 2.05

def test_div_valid_mixed():
    checker = sample.Operation()
    result = checker.div(20.0, 10.5)
    assert result == 1.9047619047619047

# Add tests for invalid types in division
def test_div_invalid_string_int():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div('Ram', 10)

def test_div_invalid_string_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div('Ram', False)

def test_div_invalid_string_float():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div('Ram', 10.2)

def test_div_invalid_int_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div(True, 10.2)

def test_div_invalid_float_bool():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div(False, 10.2)

def test_div_invalid_bools():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Value must be either an integer or a float."):
        checker.div(False, True)

# Add a test for zero division
def test_div_zero_division():
    checker = sample.Operation()
    with pytest.raises(ValueError, match="Zero division error"):
        checker.div(10, 0)
