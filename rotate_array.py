from collections import deque
from math import floor

def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)

    for i in range(n):
        row = given_array[i]
        for j in range(n):
            rotated[j][n - i - 1] = row[j]

    return rotated

def rotated_index(i, j, n):
    return j, n - i - 1

def rotate2(given_array, n):
    queue = deque()

    for i in range(floor(n/2)):
        for j in range(floor((n+1)/2)):
            queue.append(given_array[i][j])

            for _ in range(3):
                i, j = rotated_index(i, j, n)
                queue.append(given_array[i][j])
                given_array[i][j] = queue.popleft()

            i, j = rotated_index(i, j, n)
            given_array[i][j] = queue.popleft()

    return given_array


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

import unittest

class TestRotation(unittest.TestCase):
    def test_one(self):
        a1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

        result1 = [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]

        self.assertEqual(rotate2(a1, 3), result1)
