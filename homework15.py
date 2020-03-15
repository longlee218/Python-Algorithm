"""
    This problem was asked by Amazon.

    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
    Given N, write a function that returns  the number of unique ways you can climb the staircase.
    The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:
        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
    integers X? For example, if X={1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""
# step 1 or 2


def amazon_question1(number):
    if number <= 0:
        return number+1
    else:
        return amazon_question1(number-1) + amazon_question1(number-2)

# step in  set


def amazon_question2(number, steps):
    if number == 0:
        return 1
    if number < 0:
        return 0
    result = 0
    for i in steps:
        result += amazon_question2(number-i, steps)
    return result


if __name__ == '__main__':
    print(amazon_question1(4))                    # expect 5
    """
        1) [1, 1, 1, 1]
        2) [1, 2, 1]
        3) [2, 1, 1]
        4) [1, 1, 2]
        5) [2, 2]
    """
    print(amazon_question2(5, [1, 3, 5]))        # expect 5
    """
        1) [1, 1, 1, 1, 1]
        2) [3, 1, 1]
        3) [1, 3, 1]
        4) [1, 1, 3]
        5) [5]
    """
    print(amazon_question2(5, [1, 2, 3, 5]))     # expect 14
    """
        1.  [1, 1, 1, 1, 1]
        2.  [2, 1, 1, 1]
        3.  [1, 2, 1, 1]
        4.  [1, 1, 2, 1]
        5.  [1, 1, 1, 2]
        6.  [2, 2, 1]
        7.  [1, 2, 2]
        8.  [2, 1, 2]
        9.  [3, 2]
        10. [2, 3]
        11. [3, 1, 1]
        12. [1, 3, 1]
        13. [1, 1, 3]
        14. [5]
    """

"""
    Yêu cầu 1:
        - Time complexity: O(n+n/2) => O(n) n là number
        - Memory space : O(1)
        - Phân tích: F(n) = F(n-1) + F(n-2) sử dụng Fibonacy
    Yêu cầu 2:
        - Time complexity: O(n^m) m là len của set steps, n là number
        - Memory space : O(1)
        - Phân tích: F(n) = ΣF(n-i) i thuộc set st sử dụng F
"""