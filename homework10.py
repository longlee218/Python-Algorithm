"""
    This problem was asked by Stripe:

    Given an array of integers, find the first missing positive integer in
    linear time and constant space. In other words, find the lowest positive
    integer that does not exist in the array. The array can contain
    duplicate and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3
    You can modify the input array  in-place.
"""


def stripe_question(nums):
    max_number = 0
    for i in nums:
        if i > max_number:
            max_number = i
    if max_number < 0:
        return 1
    else:
        check = [False for i in range(max_number)]
        for i in range(len(nums)):
            if nums[i] > 0:
                check[nums[i]-1] = True
        for i in range(max_number):
            if check[i] is False:
                return i+1
            else:
                continue
        return max_number+1


if __name__ == '__main__':
    array1 = [3, 2, -1, 1, 2]                      # expect 4
    array2 = [1, 2, 0]                             # expect 3
    array3 = [0, -1, 0]                            # expect 1
    array4 = [1, 4, 2, 7, 3, -1, 1, 4, 2]          # expect 5
    print(stripe_question(array4))

"""

    +) Time complexity O(n+m) <n: len of nums, m: max_number in nums>    
    +) Memory space O(m) <m: max_number in nums>
--------------------------------------------------------------------------
làm ơn good đi mà, làm ơn pls :((

"""