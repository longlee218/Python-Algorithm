"""
    This problem was asked by Facebook.

    Given the mapping a=1, b=2,...z=26, and an encoded  message,
    count the number of ways it can be decoded

    For example, the messages would be 3, since it could be decoded as 'aaa','ka' and 'ak'

    You can assume that the messages are decoded. For example '001' is not allowed
"""

string = 'abcdefghijklmnopqrstuvwxyz'
string = dict(enumerate(list(''.join(string))))

# Solution 1


def check_number(list_character):
    if len(list_character) == 1 and list_character[0] == '0':
        return 0
    elif len(list_character) == 1 and 1 <= int(list_character[0]) <= 9:
        return 1
    elif len(list_character) == 2 and 10 <= int(list_character[0]+list_character[1]) <= 26:
        return 1


def fb_question(s):
    result = [0 for i in range(len(s) + 1)]
    result[0] = 1       # trường hợp chuỗi rỗng
    for i in range(len(s)):
        if check_number(s[i]) == 1:
            result[i+1] += result[i]
        if i >= 1 and check_number(s[i-1:i+1]) == 1:
            result[i+1] += result[i-1]
    return result[-1]

# Solution2


def fb_question_recur(s, index):
    if index > len(s):
        return 0
    if index == len(s):
        return 1
    a = 0
    b = 0
    if s[index] != '0':
        a = fb_question_recur(s, index+1)
    if s[index] == '1' or (s[index] == '2' and s[index] <= '6'):
        b = fb_question_recur(s, index+2)
    return a+b


if __name__ == '__main__':
    string_in = ''
    print(fb_question(string_in))
    print(fb_question_recur(string_in, 0))


"""
   Solution 1:
        +) Time complexity O(n) <n là len của chuỗi cần decode>
        +) Space memory O(n)
    Solution 2:
        +) Time complexity O(n)
        +) Space memory O(1)
"""