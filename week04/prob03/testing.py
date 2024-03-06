import unittest
from unittest.mock import patch
from main import check_one_even
import io
import sys
import random

class TestCheckOneEven(unittest.TestCase):

    def test_one_even_yes(self):
        for _ in range(50):  # Generate 50 test cases where exactly one number is even
            num1 = random.randint(1, 100) * 2  # Ensure num1 is even
            num2 = num1 + 1  # Ensure num2 is odd
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(num1, num2)
                self.assertEqual(fake_out.getvalue().strip(), "YES")

            # Swap num1 and num2 roles to cover the opposite case
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(num2, num1)
                self.assertEqual(fake_out.getvalue().strip(), "YES")

    def test_one_even_no(self):
        for _ in range(50):  # Generate 50 test cases where both numbers are either even or odd
            even_num = random.randint(1, 50) * 2
            odd_num = even_num + 1

            # Both even
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(even_num, even_num + 2)
                self.assertEqual(fake_out.getvalue().strip(), "NO")

            # Both odd
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(odd_num, odd_num + 2)
                self.assertEqual(fake_out.getvalue().strip(), "NO")

if __name__ == '__main__':
    unittest.main()
