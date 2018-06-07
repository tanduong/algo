def common_elements(list1, list2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] < list2[p2]:
            p1 += 1
        else:
            p2 += 1
    return result

import unittest

class TestCommonElement(unittest.TestCase):
    def test_one(self):
        self.assertEqual(common_elements([], []), [])

    def test_two(self):
        self.assertEqual(common_elements([1, 2], [2, 3]), [2])

    def test_three(self):
        self.assertEqual(common_elements([1, 2], [3, 4]), [])
