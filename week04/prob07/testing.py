import unittest
from unittest.mock import patch
from io import StringIO
import main
import random
import sys

# Global variable to control verbosity for test data sets
SHOW_TEST_DATA = '-v' in sys.argv

class TestSortThreeNumbers(unittest.TestCase):

    def test_random_cases(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output
        for _ in range(100):
            a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
            with patch('builtins.input', side_effect=[str(a), str(b), str(c)]), patch('sys.stdout', new=StringIO()) as fake_out:
                main.sort_three_numbers(int(input()), int(input()), int(input()))
                output = list(map(int, fake_out.getvalue().strip().split()))
                expected_output = sorted([a, b, c])
                self.assertEqual(output, expected_output)
                if SHOW_TEST_DATA:
                    sys.stdout = original_stdout  # Reset stdout to original
                    print(f'Test data: {a}, {b}, {c} | Expected: {expected_output} | Got: {output}')
        sys.stdout = original_stdout  # Ensure stdout is reset to original after all tests

if __name__ == '__main__':
    # Remove our custom flag before unittest processes command line arguments
    if SHOW_TEST_DATA:
        sys.argv.remove('-v')
    unittest.main()
