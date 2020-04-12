"""
    Find the second largest node in binary search tree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return ''.format(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert_bst(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_bst(self.root, data)

    def _insert_bst(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert_bst(root.left, data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert_bst(root.right, data)
        elif data == root.data:
            return

    def display(self):
        if self.root:
            self._display(self.root)

    def _display(self, root):
        if root is not None:
            self._display(root.left)
            print(root.data)
            self._display(root.right)


def second_largest_bst(root):
    while root:
        if root.left is not None and root.right is None:
            root = root.left
            while root.right is not None:
                root = root.right
            return root.data
        elif root.right is not None and root.right.right is None and root.right.left is None:
            return root.data
        root = root.right


if __name__ == '__main__':
    tree = BST()
    tree.insert_bst(10)
    tree.insert_bst(5)
    tree.insert_bst(18)
    tree.insert_bst(3)
    tree.insert_bst(6)
    tree.insert_bst(1)
    tree.insert_bst(4)
    tree.insert_bst(7)
    # tree.insert_bst(18)
    tree.insert_bst(15)
    # tree.insert_bst(20)
    # tree.insert_bst(11)
    # tree.insert_bst(16)
    # tree.insert_bst(19)
    print(second_largest_bst(tree.root))

"""
    +) Time complexity: O(n*log(n)) <n = number of nodes>
    +) Memory space: O(n)
"""