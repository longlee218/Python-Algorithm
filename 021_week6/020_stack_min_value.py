"""
    Create simple stack which supports push, pop, top, and retrieving the minimum element in
    constant time.

    push(x): push element into stack.
    pop(): remove the element on top of stack.
    top(): return the element on top of stack.
    getMin(): retrieving the minimum value of stack.

"""


class MinStack(object):
    def __init__(self):
        self.stack = []

    def isNull(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isNull():
            return False
        self.stack.pop()

    def top(self):
        if self.isNull():
            return None
        return self.stack[-1]

    def getMin(self):
        if self.isNull():
            return None
        return min(self.stack)


if __name__ == '__main__':
    x = MinStack()
    x.push(-2)
    x.push(0)
    x.push(-3)
    print(x.getMin())
    x.pop()
    print(x.top())
    print(x.getMin())

"""
    Time complexity: O(1)
    
"""