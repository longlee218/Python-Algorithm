"""
    Run-length encoding is a fast and simple method of encoding strings
    the basic idea is to represent repeated successive characters as
    a single count and character. For example, the string:
    "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

    Implement run-length encoding and decoding. You can assume the
    string to be encoded have no digits and consists solely of
    alphabetic character. You can assume the string to be decoded is valid
"""


def solve(strings):
    strings = strings+'*'
    count = 1
    result = []
    for i in range(len(strings)-1):
        if strings[i] == strings[i+1]:
            count += 1
            continue
        result.append(str(count)+strings[i])
        count = 1
    return ''.join(result)


if __name__ == '__main__':
    string = 'AAAABBBCCDAA'
    print(solve(string))

"""
    +) Time complexity: O(n) <n = len of string>
"""