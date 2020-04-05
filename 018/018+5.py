"""
    Given a singly linked list and an integer K, remove Kth last element
    from the list, K is guaranteed to be smaller than the length of
    the list.
    The list is very long, so making more than one pass is prohibitively
    expensive.
    Do this in constant space and in one pass

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node_new = Node(value)
        node_new.next = self.head
        self.head = node_new

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    def count(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def remove(self, k):
        prev = None
        count = 0
        node = self.head
        while node is not None:
            if count == self.count() - k:
                break
            prev = node
            count += 1
            node = node.next
        if prev is None:
            self.head = node.next
            del node
            return
        elif prev.next is None:
            return
        else:
            prev.next = node.next
            del node


if __name__ == '__main__':
    linklist = Linklist()
    linklist.insert(5)
    linklist.insert(4)
    linklist.insert(3)
    linklist.insert(2)
    linklist.insert(1)
    linklist.display()
    linklist.remove(2)

    print("\n")
    linklist.display()