"""
    A look-and-say sequence is defined as the integer sequence beginning with a single
    digit in which the next term is obtained by describing the previous term. An example is
    easier to understand

    Example:
            1
            11
            21
            1211
            111221
            312211
"""


def look_and_say(string):
    result = []
    index = 0
    while index < len(string):
        count = 1
        while index+1 < len(string) and string[index] == string[index+1]:
            count += 1
            index += 1
        result.append(str(count)+string[index])
        index += 1
    return result


def solve(n):
    string = '1'
    if n == 1:
        return string
    else:
        for _ in range(n-1):
            string = look_and_say(string)
    return ''.join(string)


if __name__ == '__main__':
    n = 3
    print(solve(n))