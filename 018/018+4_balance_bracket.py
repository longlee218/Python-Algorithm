"""
    Given a strong of round, curly and square and closing bracket
    return whether the bracket are balance.
    For example, given the string "([])[]({})" you should return true
    given the string"[]{)" or "((()" return false.
"""


def solve(strings):
    stack = []
    for i in range(len(strings)):
        if strings[i] == '(' or strings[i] == '{' or strings[i] == '[':
            stack.append(strings[i])
        elif len(stack) != 0 and ((stack[-1] == '(' and strings[i] == ')')
                                  or (stack[-1] == '[' and strings[i] == ']')
                                  or (stack[-1] == '{' and strings[i] == '}')):
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    return False


if __name__ == '__main__':
    string = '([])[]({})'
    print(solve(string))

"""
    +) Time complexity: O(n) < n = len string >
"""