"""
    Two words can be 'chained' if the last character of the first word is the same as the first
    character of the second word.

    Given a list of words, determine if there is a way to 'chain' all the words in a circle.

    Example:
        Input: ['eggs', 'karat', 'apple', 'snack', 'tuna' ]
        Output: True
"""

import collections


def ChainedWord(words):
    if words is None:
        return False
    diction = {}
    for i in words:
        if i is None:
            return False
        start, end = i[0], i[-1]
        if start not in diction:
            diction[start] = {}
        if end not in diction[start]:
            diction[start][end] = 0
        diction[start][end] += 1
    if len(diction) == 0:
        return True
    first_character = next(iter(diction))
    stack = [first_character]
    while len(diction) > 0:
        next_character = stack.pop()
        if next_character not in diction:
            return False
        last_character = next(iter(diction[next_character]))
        diction[next_character][last_character] -= 1
        if diction[next_character][last_character] <= 0:
            del diction[next_character][last_character]
            if len(diction[next_character]) == 0:
                del diction[next_character]
            stack.append(last_character)
    if len(diction) == 0 and stack.pop() == first_character:
        return True


if __name__ == '__main__':
    print(ChainedWord(words=['axb', 'bxc', 'cxd', 'dxe', 'dxa', 'exd']))

"""
    +) Time complexity: O(n^2)
"""