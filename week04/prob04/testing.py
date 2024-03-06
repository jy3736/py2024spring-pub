import unittest
from unittest.mock import patch
from main import check_ascending_order
import io
import sys
import random

class TestCheckAscendingOrder(unittest.TestCase):

    def test_ascending_order_yes(self):
        for _ in range(50):  # Generate 50 test cases where the condition is true
            num1 = random.randint(1, 30)
            num2 = num1 + random.randint(1, 10)  # Ensure num2 is greater than num1
            num3 = num2 + random.randint(1, 10)  # Ensure num3 is greater than num2
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_ascending_order(num1, num2, num3)
                self.assertEqual(fake_out.getvalue().strip(), "YES")

    def test_ascending_order_no(self):
        for _ in range(50):  # Generate 50 test cases where the condition is false
            num1 = random.randint(31, 60)
            num2 = num1 - random.randint(1, 10)  # Ensure num2 is less than num1
            num3 = num2 - random.randint(1, 10)  # Ensure num3 is less than num2
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_ascending_order(num1, num2, num3)
                self.assertEqual(fake_out.getvalue().strip(), "NO")

            # Also test for non-strict inequality
            num2 = num1
            num3 = num2 + random.randint(1, 10)
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                check_ascending_order(num1, num2, num3)
                self.assertEqual(fake_out.getvalue().strip(), "NO")

if __name__ == '__main__':
    unittest.main()
