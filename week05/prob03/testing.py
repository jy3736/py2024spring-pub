import unittest
from unittest.mock import patch
import io
import random
import os, sys

#current_directory = os.getcwd()
#if current_directory not in sys.path:
#   sys.path.append(current_directory)

from main import find_closest_distance

class TestFindClosestDistance(unittest.TestCase):

    def test_closest_distance(self):
        for _ in range(100):  # Generate 100 random test cases
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            expected_closest_distance = min(abs(a - b), abs(a - c))

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                find_closest_distance(a, b, c)
                output = int(fake_out.getvalue().strip())
                self.assertEqual(output, expected_closest_distance, f"Failed for {a}, {b}, {c}")

if __name__ == '__main__':
    unittest.main()