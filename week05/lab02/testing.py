import unittest
from unittest.mock import patch
import io
import random
import os, sys

#current_directory = os.getcwd()
#if current_directory not in sys.path:
#   sys.path.append(current_directory)

from main import check_divisible_by_four


class TestCheckDivisibleByFour(unittest.TestCase):

    def test_check_divisible_by_four_yes(self):
        for _ in range(50):  # Generate 50 test cases where the condition is true
            number = random.randint(1, 100) * 4  # Ensure the number is divisible by 4
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_divisible_by_four(number)
                self.assertEqual(fake_out.getvalue().strip(), "YES", f"Failed for {number}")

    def test_check_divisible_by_four_no(self):
        for _ in range(50):  # Generate 50 test cases where the condition is false
            number = random.randint(1, 100) * 4 + random.choice([1, 2, 3])  # Ensure the number is not divisible by 4
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_divisible_by_four(number)
                self.assertEqual(fake_out.getvalue().strip(), "NO", f"Failed for {number}")

if __name__ == '__main__':
    unittest.main()
