import unittest

from calculator import evaluate_expression


class EvaluateExpressionTests(unittest.TestCase):
    def test_operator_precedence_and_parentheses(self):
        self.assertEqual(evaluate_expression("2 + 3 * (4 - 1)"), 11)

    def test_unary_operators_and_division(self):
        self.assertEqual(evaluate_expression("-8 / +2"), -4)

    def test_rejects_unsupported_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("__import__('os').system('echo unsafe')")

    def test_reports_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("1 / 0")


if __name__ == "__main__":
    unittest.main()
