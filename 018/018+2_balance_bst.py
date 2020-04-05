"""
    This problem was asked by Linkedin:
    Given a sort list of numbers, change it into balance binary search
    tree. You can assume there will be no duplicate numbers in the list
"""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalanceBST(nums):
    if len(nums) <= 0:
        return None
    else:
        mid = int(len(nums)/2)
        root_mid = Node(nums[mid])
        root_mid.left = createBalanceBST(nums[:mid])
        root_mid.right = createBalanceBST(nums[mid+1:])
        return root_mid


if __name__ == '__main__':
    print(createBalanceBST([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""
    +) Time complexity: O(log(n)) <n = len of nums>
"""