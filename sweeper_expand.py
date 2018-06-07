from collections import deque

def valid_cell_index(a, b, num_rows, num_cols):
    return 0 <= a < num_rows and 0 <= b < num_cols

def connected_cells(cell, num_rows, num_cols):
    return ((a, b) for a in range(cell[0] - 1, cell[0] + 2)
                   for b in range(cell[1] - 1, cell[1] + 2)
                   if valid_cell_index(a, b, num_rows, num_cols))

def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] == -1:
        return field

    queue = deque()
    queue.append((given_i, given_j))

    while queue:
        cell = queue.popleft()
        cell_value = field[cell[0]][cell[1]]
        if cell_value != 0:
            continue

        field[cell[0]][cell[1]] = -2
        for connected_cell in connected_cells(cell, num_rows, num_cols):
            connected_cell_value = field[connected_cell[0]][connected_cell[1]]
            if connected_cell_value != -1 and connected_cell_value != -2:
                queue.append(connected_cell)

    return field


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

import unittest

class TestRotation(unittest.TestCase):
    def test_one(self):
        field1 = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 1, -1, 1, 0]]

        result1 = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 1, -1, 1, 0]]

        self.assertEqual(click(field1, 3, 5, 2, 2), result1)

        result2 = [[-2, -2, -2, -2, -2],
                   [-2, 1, 1, 1, -2],
                   [-2, 1, -1, 1, -2]]

        print(to_string(click(field1, 3, 5, 1, 4)))
        print(to_string(result2))
        self.assertEqual(click(field1, 3, 5, 1, 4), result2)
