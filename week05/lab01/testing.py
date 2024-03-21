import unittest
from unittest.mock import patch
import io
import os, sys

#current_directory = os.getcwd()
#if current_directory not in sys.path:
#   sys.path.append(current_directory)
    
from main import check_last_digit


class TestCheckLastDigit(unittest.TestCase):
    
    def test_check_last_digit(self):
        test_cases = [i for i in range(100)]
        expected_outputs = [("YES" if x % 10 == 7 else "NO") + "\n" for x in test_cases]
        
        for input_val, expected_output in zip(test_cases, expected_outputs):
            with self.subTest(input=input_val, expected_output=expected_output):
                with patch('sys.stdout', new=io.StringIO()) as fake_out:
                    with patch('builtins.input', return_value=str(input_val)):
                        check_last_digit(int(input()))
                        self.assertEqual(fake_out.getvalue(), expected_output, f"Failed for {input_val}")

if __name__ == '__main__':
    unittest.main()
