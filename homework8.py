"""
    Hi, here's your problem today. This problem was recently asked by Apple:
    You are given two singly linked lists. The lists intersect at some node.
    Find and return a node. Note: the lists are non:cyclical

    Example:

        A = 1->2->3->4
        B = 6->3->4

        This should return 3 (you may assume that any nodes with the same value are the same node).
        Here is a starting point:

        def intersection(a, b):
            #fill this in.

        class Node:
            def __init__(self, val):
                self.val = val
                self.next = None

            def pretty_print(self):
                c = self
                while c:
                    print(c.val)
                    c = c.next
        a = Node(1)
        a.next = Node(2)
        a.next.next = Node(3)
        a.next.next.next = Node(4)

        b = Node(6)
        b.next = a.next.next
        c = intersection(a, b)
        c.pretty_print()
        # 3 4
"""


def intersection(a, b):
    nodes_intersection = []
    A = a
    B = b
    while A is not None:
        nodes_intersection.append(A.val)
        A = A.next
    while B is not None:
        if B.val in nodes_intersection:
            return B
        B = B.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def pretty_print(self):
        c = self
        while c:
            print(c.val)
            c = c.next


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next
    b.next.next.next = Node(7)

    c = intersection(a, b)
    c.pretty_print()

"""
    +) Độ phức tạp thời gian O(n*m) với n: số node của a, m: số node của b
    +) Space memory là O(n) với n: số node của a
"""