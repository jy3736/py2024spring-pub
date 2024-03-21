import unittest
from unittest.mock import patch
import io
import random
import os, sys

#current_directory = os.getcwd()
#if current_directory not in sys.path:
#   sys.path.append(current_directory)
from main import check_one_even

class TestCheckOneEven(unittest.TestCase):

    def test_one_even_yes(self):
        for _ in range(50):  # Generate 50 test cases where exactly one number is even
            num1 = random.randint(1, 100) * 2  # Ensure num1 is even
            num2 = num1 + 1  # Ensure num2 is odd
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(num1, num2)
                self.assertEqual(fake_out.getvalue().strip(), "YES", f"Failed for {num1} and {num2}")

            # Swap num1 and num2 roles to cover the opposite case
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(num2, num1)
                self.assertEqual(fake_out.getvalue().strip(), "YES", f"Failed for {num2} and {num1}")

    def test_one_even_no(self):
        for _ in range(50):  # Generate 50 test cases where both numbers are either even or odd
            even_num = random.randint(1, 50) * 2
            odd_num = even_num + 1

            # Both even
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(even_num, even_num + 2)
                self.assertEqual(fake_out.getvalue().strip(), "NO", f"Failed for {even_num} and {even_num + 2}")

            # Both odd
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_one_even(odd_num, odd_num + 2)
                self.assertEqual(fake_out.getvalue().strip(), "NO", f"Failed for {odd_num} and {odd_num + 2}")

if __name__ == '__main__':
    unittest.main()
