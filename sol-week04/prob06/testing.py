import unittest
from unittest.mock import patch
from main import find_closest_distance
import io
import sys
import random

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
                self.assertEqual(output, expected_closest_distance)

if __name__ == '__main__':
    unittest.main()
