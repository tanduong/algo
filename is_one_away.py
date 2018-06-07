def is_one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    p1 = 0
    p2 = 0
    edited = False
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif not edited:
            edited = True
            if len(s1) > len(s2):
                p1 += 1
            elif len(s1) < len(s2):
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        else:
            return False
    return True


import unittest

class TestRotation(unittest.TestCase):
    def test_one(self):
        self.assertEqual(is_one_away("abcde", "abcd"), True)

    def test_four(self):
        self.assertEqual(is_one_away("abcdef", "abccef"), True)

    def test_two(self):
        self.assertEqual(is_one_away("abde", "abcde"), True)

    def test_three(self):
        self.assertEqual(is_one_away("a", "a"), True)
