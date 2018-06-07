
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# Implement your function below.
def is_bst(node, lower_lim=None, upper_lim=None):
    try:
        assert not lower_lim or node.value > lower_lim, \
            'Node %r is less than lower_lim %r' % (node.value, lower_lim)
        assert not upper_lim or node.value < upper_lim, \
            'Node %r is more than upper_lim %r' % (node.value, upper_lim)

        left_upper_lim = min(upper_lim, node.value) if upper_lim else node.value
        assert not node.left or is_bst(node.left, lower_lim=lower_lim, upper_lim=left_upper_lim), \
            'Left tree of %r is not a bst' % node.value

        right_lower_lim = max(lower_lim, node.value) if lower_lim else node.value
        assert not node.right or is_bst(node.right, lower_lim=right_lower_lim, upper_lim=upper_lim), \
            'Right tree of %r is not a bst' % node.value

        return True
    except AssertionError as exception:
        # print(str(exception))
        return False

def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

import unittest

class TestRotation(unittest.TestCase):

    def test_one(self):
        self.assertEqual(is_bst(head3), True)

    def test_two(self):
        self.assertEqual(is_bst(head1), False)

    def test_three(self):
        self.assertEqual(is_bst(head2), False)

    def test_four(self):
        self.assertEqual(is_bst(head4), False)
