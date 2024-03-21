import unittest
import os, sys

#current_directory = os.getcwd()
#if current_directory not in sys.path:
#   sys.path.append(current_directory)
    
from main import count_unique

def _count_unique(numstr):
    numbers = numstr.split()
    unique = []
    for item in numbers:
        if item not in unique:
            unique.append(item)
    count = len(unique)
    return count
    
data = [
    "1 2 3 4 5 6 7 8 9",
    "1 1 1 1 1 1 1 1",
    "1 2 1 2 1 2 1 2",
    "1 2 3 1 2 3 1 2 3",
    "1 1 1 1 2",
    "1 2 2 3 3 4",
    "1 1 1 2 2 2 3 3 3",
    "2 2 3 3 4 4 5 5 6",
    "1 1 1 1 2 2 2 2 3",
    "1 2 2 3 3 4 4 5 5",
    "1 2 1 2 3 1 2 3 4",
    "1 2 3 1 2 3 4 1 2",
    "1 2 3 4 5 1 2 3 4",
    "1 2 3 4 1 2 3 4 5",
    "1 2 3 4 5 6 1 2 3",
    "1 2 3 4 5 1 2 3 4",
    "1 2 3 4 1 2 3 4 5",
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15",
    "5 4 3 2 1",
    "2 4 6 8 10 12 14",
    "3 1 4 1 5 9 2 6 5 3 5 9",
    "7 7 7 7 7 7 7 7",
    "3 2 1 2 3 4 5 6",
    "9 8 7 6 5 4 3 2 1",
    "10 20 30 40 50 60 70 80 90 100 110 120 130 140 150",
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15",
    "5 5 5 5 5 5 5 5 5 5",
    "2 2 2 2 2 2 2 2 2 2 2 2 2 2 2",
    "3 3 3 3 3 3 3 3 3 3 3 3 3 3 3",
    "4 4 4 4 4 4 4 4 4 4 4 4 4 4 4",
    "6 6 6 6 6 6 6 6 6 6 6 6 6 6 6",
]

class Testing(unittest.TestCase):
    
    def test_all(self):
        global data
        for s in data:
            print(f"\"{s}\"")
            self.assertEqual(count_unique(s), _count_unique(s), f"Failed for {s}")


if __name__ == '__main__':
    unittest.main()

