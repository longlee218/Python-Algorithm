"""
    You are given a BST representation of an arithmetic expression. In this tree, each leaf is an integer
    value, and a non-leaf node is one of the four operations:  '+', '-', '*', '/'.

    Write a function that tales this tree and evaluates the expression.

    Example:
            *
          /   \
         +     +
        / \   / \
       3   2  4  5

    (3+2)*(4+5) = 45
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(root):
    if not (root.left and root.right):
        return int(root.val)
    left = evaluate(root.left)
    right = evaluate(root.right)
    if root.val == '+':
        return left+right
    elif root.val == '-':
        return left-right
    elif root.val == '*':
        return left*right
    elif root.val == '/':
        return left/right


def print_tree(root):
    if root:
        if root.left is not None and root.left.left is None:
            print('(', end='')
        print_tree(root.left)
        print(root.val, end='')
        print_tree(root.right)
        if root.right is not None and root.right.right is None:
            print(')', end='')
    return ' = '


if __name__ == '__main__':
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    tree = Node(TIMES)
    tree.left = Node(PLUS)
    tree.right = Node(PLUS)
    tree.left.left = Node(-3)
    tree.left.right = Node(2)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    print(print_tree(tree), end='')
    print(evaluate(tree))

"""
    +) Time complexity: O(n*log(n)) (n là chiều cao của cây)
"""