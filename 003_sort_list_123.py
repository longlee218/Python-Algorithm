"""
    Given a list of numbers with only 3 unique numbers (1,2,3), sort the list in O(n) time

    Example:
        Input: [3, 2, 1, 1, 3, 3, 2, 2]
        Output: [1, 1, 2, 2, 2, 3, 3, 3]

"""


def sort_num(nums):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in nums:
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        else:
            count3 += 1
    array1 = [1]*count1
    array2 = [2]*count2
    array3 = [3]*count3
    result = array1 + array2 + array3
    return result


if __name__ == '__main__':
    array = [1, 3, 2, 1, 1, 2, 3, 1]
    print(sort_num(array))
