import unittest
from collections import Counter

def most_frequent(arr):
    try:
        return Counter(arr).most_common(1)[0][0]
    except:
        return None

class TestMostFrequent(unittest.TestCase):
    def test_one(self):
        self.assertEqual(most_frequent([1, 2, 3, 1, 2, 1]), 1)

    def test_two(self):
        self.assertEqual(most_frequent([1, 2, 2]), 2)

    def test_three(self):
        self.assertEqual(most_frequent([3]), 3)

    def test_four(self):
        self.assertEqual(most_frequent([]), None)

if __name__ == '__main__':
    unittest.main()
