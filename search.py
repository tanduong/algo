import unittest
from functools import lru_cache

def count_sets_dp(arr, total):
    @lru_cache(maxsize=None)
    def dp(total, i):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif i < 0:
            return 0
        elif total < arr[i]:
            return dp(total, i - 1)
        else:
            return dp(total - arr[i], i - 1) + dp(total, i - 1)
    return dp(total, len(arr) - 1)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(count_sets_dp([2, 4, 6, 10], 16), 2)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
