import unittest
from unittest.mock import patch
from main import determine_square_color
import io
import random

class TestDetermineSquareColor(unittest.TestCase):

    def test_random_square_colors(self):
        for _ in range(100):  # Generate 100 random test cases
            column = random.randint(1, 8)
            row = random.randint(1, 8)
            expected_output = "BLACK" if (column + row) % 2 == 0 else "WHITE"

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                determine_square_color(column, row)
                self.assertEqual(fake_out.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
