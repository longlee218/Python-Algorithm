"""
    Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

    Example:
        Input: [0, 1, 2, 5, 7, 8, 9, 10, 11, 15]
        Output: ['0->2', '5->5, '7->11', '15->15']

    Assume that all numbers will be greater than of equal to 0, and each element can repeat.
    Here is a starting point:


    def findRanges(nums):
        #fill this

    print(findRanges([0, 1, 2, 5, 7, 8, 9, 10, 11, 15]))
    #['0->2', '5->5, '7->11', '15->15']
"""


def findRanges(nums):
    index = 0
    result = []
    string = ''
    while index < len(nums):
        string = string+str(nums[index]) + '->'
        while index < len(nums)-1 and nums[index]+1 == nums[index+1]:
            index += 1
        string = string+str(nums[index])
        result.append(string)
        string = ''
        index += 1
    return result


if __name__ == '__main__':
    array = [0, 1, 2, 5, 7, 8, 9, 10, 11, 15]
    print((findRanges(array)))

"""
    +) Time complexity: O(n) <n = len of nums>
    +) Memory space: O(n)
"""