
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):
        if self.root:
            self.print_tree_specific(self.root)

    def print_tree_specific(self, current_node):
        if current_node:
            self.print_tree_specific(current_node.left)
            print(current_node)
            self.print_tree_specific(current_node.right)

    def insert_bst(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_specific(value, self.root)

    def insert_specific(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert_specific(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_specific(value, current_node.right)
        elif value == current_node.value:
            print('Value exist')

    def search(self, value_find):
        if self.root is None:
            print('Cannot find')
            return False
        if self.root is not None:
            self.search_specific(self.root, value_find)

    def search_specific(self, current_node, value_find):
        if value_find == current_node.value:
            print('Find it')
            return True
        elif value_find < current_node.value:
            self.search_specific(current_node.left, value_find)
        elif value_find > current_node.value:
            self.search_specific(current_node.right, value_find)
        else:
            print('Cannot find')
            return False

    # def left_most(self, current):
    #     while current.left is not None:
    #         current = current.left
    #     return current
    #
    # def delete_node(self, root, value):
    #     if root is None:
    #         return root
    #     if value < root.value:
    #         root.left = self.delete_node(root.left, value)
    #     elif value > root.value:
    #         root.right = self.delete_node(root.right, value)
    #     else:
    #         if root.left is None:
    #             new = Node(root.right.value)
    #             del root
    #             return new
    #         if root.right is None:
    #             new = Node(root.left.value)
    #             del root
    #             return new
    #         root.value = self.left_most(root.right)
    #         root.right = self.delete_node(root.right, root.value)
    #     return root


def way_root_to_value(root, value, listed):
    if root is None:
        return False
    listed.append(root.value)
    if root.value == value:
        return True
    elif way_root_to_value(root.left, value, listed) or \
            way_root_to_value(root.right, value, listed):
        return True
    else:
        listed.pop()
        return False


def amazon_question(tree_default, value1, value2):
    listed1 = []
    listed2 = []
    way_root_to_value(tree_default.root, value1, listed1)
    way_root_to_value(tree_default.root, value2, listed2)
    if (value2 > tree_default.root.value and value1 > tree_default.root.value) \
        or (value1 < tree_default.root.value and value2 < tree_default.root.value):
        index_listed1 = 0
        index_listed2 = 0
        listed1.remove(value1)
        while index_listed1 < len(listed1) or index_listed2 < len(listed2):
            if index_listed2 == index_listed1 and listed1[index_listed1] == listed2[index_listed2]:
                index_listed1 += 1
                index_listed2 += 1
            else:
                break
        listed1 = listed1[index_listed1-1:len(listed1)+1]
        listed2 = listed2[index_listed2:len(listed2)+1]
        result = listed1[::-1]+listed2
        return len(result)
    else:
        listed1.remove(tree_default.root.value)
        result = listed1[::-1] + listed2
        return len(result)


def facebook_question(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is not None and root2 is None) or (root1 is None and root2 is not None):
        return False
    else:
        if root1.value == root2.value and \
                facebook_question(root1.left, root2.left) and \
                facebook_question(root1.right, root2.right):
            return True
        else:
            return False


if __name__ == '__main__':
    tree1 = BST()
    tree2 = BST()
    tree1.insert_bst(10)
    tree1.insert_bst(5)
    tree1.insert_bst(15)
    tree1.insert_bst(3)
    tree1.insert_bst(7)
    tree1.insert_bst(15)
    tree1.insert_bst(11)
    tree1.insert_bst(16)
    tree1.insert_bst(2)
    tree1.insert_bst(1)

    tree2.insert_bst(8)
    tree2.insert_bst(6)
    tree2.insert_bst(10)
    tree2.insert_bst(5)
    tree2.insert_bst(12)
    tree2.insert_bst(9)
    tree2.insert_bst(7)

    # tree2.print_tree()
    # print(facebook_question(tree1.root, tree1.root))
    # print(facebook_question(tree1.root, tree2.root))
    #
    # print(amazon_question(tree1, 2, 7))
