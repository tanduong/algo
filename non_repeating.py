
from collections import Counter

def non_repeating(given_string):
    counter = Counter(given_string)
    for c in given_string:
        if counter[c] == 1:
          return c
    return None

import unittest

class TestCounter(unittest.TestCase):
    def test_one(self):
        self.assertEqual(non_repeating("abcab"), 'c')
