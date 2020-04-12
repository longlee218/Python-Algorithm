
"""
    The power set of a set is the set of all its subsets.
    Write a function that given a set, generates its power set.
    For example, given the set {1, 2, 3}, it should return
    {{}, {1}, {2], {3}, {1, 2}, {1, 3}, {2, 3}, {1,2,3}}

"""


def solve(arr):
    arr = list(arr)
    result = [[]]
    for i in arr:
        result.extend([sub + list([i]) for sub in result])
    return result


if __name__ == '__main__':
    array = {1, 2, 3}
    print(solve(array))

"""
    +) Time complexity: O(n*log(n)) <n = number of array>
    +) Memory space: O(n)
"""