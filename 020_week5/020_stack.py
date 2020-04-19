"""
    Implement a stack that has the following methods:

    +) push(val): which pushes an element onto the stack.
    +) pop(): which pop off and returns the topmost element of the stack. If there are no elements
    in the stack. If there are no elements in the stack, then it should throw an error or return null.
    +) max(): which returns the maximum value in the stack currently. If there are no elements in the stacks,
    then it should throw an error or return null

    Each method should run in constant time.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def print_stack(self):
        return self.stack

    @staticmethod
    def is_emp(stack):
        if not stack:
            return True
        return False

    def pop(self):
        if self.is_emp(self.stack):
            return None
        return self.stack.pop()

    def max_in_stack(self):
        if self.is_emp(self.stack):
            return None
        return max(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.print_stack())

    print(stack.max_in_stack())
    stack.pop()
    print(stack.print_stack())