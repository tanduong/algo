def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    length = len(list1)

    def is_rotation_by(shifted):
        return all(list1[i] == list2[(i+shifted) % length] for i in range(length))

    # return any(is_rotation_by(i) for i in range(length))
    return is_rotation_by(list2.index(list1[0]))

import unittest

class TestRotation(unittest.TestCase):
    def test_one(self):
        self.assertEqual(is_rotation([1, 2, 3], [2, 3, 1]), True)

    def test_two(self):
        self.assertEqual(is_rotation([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]), True)

    def test_three(self):
        self.assertEqual(is_rotation([1, 2, 3], [3, 1, 2]), True)
