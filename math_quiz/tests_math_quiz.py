import unittest
from math_quiz import get_random_integer, get_random_operator, generate_math_problem

class TestMathQuizFunctions(unittest.TestCase):

    def test_get_random_integer(self):
        # Test that the generated random integer is within the specified range.
        min_value = 1
        max_value = 10
        random_num = get_random_integer(min_value, max_value)
        self.assertTrue(min_value <= random_num <= max_value)

    def test_get_random_operator(self):
        # Test that the random operator is one of the expected operators.
        operators = ['+', '-', '*']
        random_op = get_random_operator()
        self.assertIn(random_op, operators)

    def test_generate_math_problem(self):
        # Test that the generated math problem and answer match the expected format.
        problem, answer = generate_math_problem()
        num1, operator, num2 = problem.split()
        num1 = int(num1)
        num2 = int(num2)

        if operator == '+':
            expected_answer = num1 + num2
        elif operator == '-':
            expected_answer = num1 - num2
        else:
            expected_answer = num1 * num2

        self.assertEqual(int(answer), expected_answer)

if __name__ == '__main__':
    unittest.main()
