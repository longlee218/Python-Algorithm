"""
    Given a string with certain rule: k[string] should be expanded to string k times.
    So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen,
    so 2[a2[b]c] should be expanded to abbcabbc.

"""


def decode(s):
    stack = []
    number = 0
    cur_string = ''
    for i in s:
        if i == '[':
            stack.append(number)
            stack.append(cur_string)
            number = 0
            cur_string = ''
        elif i == ']':
            string = stack.pop()
            number_get = stack.pop()
            cur_string = string + number_get*cur_string
        elif i.isdigit():
            number = number*10 + int(i)
        else:
            cur_string += i
    return cur_string


if __name__ == '__main__':
    print(decode('2[ab3[b]c]'))

"""
    Time complexity: O(n) <n len of string>
"""