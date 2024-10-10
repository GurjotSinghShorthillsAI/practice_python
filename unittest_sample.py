import unittest
import sample

class TestSample(unittest.TestCase):  

    def setUp(self):
        self.checker = sample.Operation()

    def test_add_valid_integers(self):
        result = self.checker.add(10, 20)
        self.assertEqual(result, 30)

    def test_add_valid_floats(self):
        result = self.checker.add(10.5, 20.5)
        self.assertEqual(result, 31.0)

    def test_add_valid_mixed(self):
        result1 = self.checker.add(10, 20.5)
        self.assertEqual(result1, 30.5)

    def test_add_invalid_string_int(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add('Ram', 10)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_add_invalid_string_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add('Ram', False)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_add_invalid_string_float(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add('Ram', 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_add_invalid_int_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add(True, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_add_invalid_float_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add(False, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_add_invalid_bools(self):
        with self.assertRaises(ValueError) as context:
            self.checker.add(False, True)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_valid_integers(self):
        result = self.checker.minus(20, 10)
        self.assertEqual(result, 10)

    def test_minus_valid_floats(self):
        result = self.checker.minus(20.5, 10.5)
        self.assertEqual(result, 10.0)

    def test_minus_valid_mixed(self):
        result = self.checker.minus(20, 10.5)
        self.assertEqual(result, 9.5)

    def test_minus_invalid_string_int(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus('Ram', 10)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_invalid_string_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus('Ram', False)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_invalid_string_float(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus('Ram', 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_invalid_int_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus(True, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_invalid_float_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus(False, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus_invalid_bools(self):
        with self.assertRaises(ValueError) as context:
            self.checker.minus(False, True)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_valid_integers(self):
        result = self.checker.mul(10, 20)
        self.assertEqual(result, 200)

    def test_mul_valid_floats(self):
        result = self.checker.mul(10.5, 20.0)
        self.assertEqual(result, 210.0)

    def test_mul_valid_mixed(self):
        result = self.checker.mul(10, 20.5)
        self.assertEqual(result, 205.0)

    def test_mul_invalid_string_int(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul('Ram', 10)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_invalid_string_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul('Ram', False)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_invalid_string_float(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul('Ram', 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_invalid_int_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul(True, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_invalid_float_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul(False, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul_invalid_bools(self):
        with self.assertRaises(ValueError) as context:
            self.checker.mul(False, True)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_valid_integers(self):
        result = self.checker.div(20, 10)
        self.assertEqual(result, 2)

    def test_div_valid_floats(self):
        result = self.checker.div(20.5, 10.0)
        self.assertEqual(result, 2.05)

    def test_div_valid_mixed(self):
        result = self.checker.div(20.0, 10.5)
        self.assertEqual(result, 1.9047619047619047)  # Expecting float result

    def test_div_invalid_string_int(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div('Ram', 10)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_invalid_string_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div('Ram', False)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_invalid_string_float(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div('Ram', 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_invalid_int_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div(True, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_invalid_float_bool(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div(False, 10.2)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_invalid_bools(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div(False, True)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div_zero_division(self):
        with self.assertRaises(ValueError) as context:
            self.checker.div(10, 0)
        self.assertEqual(str(context.exception), "Zero division error")


if __name__ == "__main__":
    unittest.main()
