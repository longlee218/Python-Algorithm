"""
    This problem was asked by Uber:

    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in the
    original array except the one at i

    For example, if our input was [1, 2, 3, 4, 5] , the expected
    output would be [123, 60, 40, 30, 24] . If our input was
    [3, 2, 1], the expected output would be [2, 3, 6]

    Follow-up: what if you can't use division?
"""


def uber_question(nums):
    new_array = []
    element = 1
    i = 0
    while i < len(nums):
        for j in range(len(nums)):
            if j == i:
                continue
            element *= nums[j]
        new_array.append(element)
        element = 1
        i += 1
    return new_array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    array2 = [3, 2, 1]
    print(uber_question(array))
    print(uber_question(array2))

"""
    *Solution
       +) Độ phức tạp thuật toán O(n^2) với n là len của chuỗi số đầu vào
       +) Memory space O(n^2) với n là len của chuỗi số đầu vào
"""