"""
    This problem was asked by Airbnb

    Given a list of integer, write a function that returns the largest sum of non-adjacent numbers.
    Number can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
    should return 10, since we pick 5 and 5.

    Follow-up: Can you do this in O(n) time and constant space?

"""


def max_number(number1, number2):
    if number1 > number2:
        return number1
    return number2


def airbnb_question(nums):
    sum_adjacent = nums[0]
    sum_non_adjacent = 0
    for i in range(1, len(nums)):
        temp = max_number(sum_adjacent, sum_non_adjacent)
        sum_adjacent = nums[i] + sum_non_adjacent
        sum_non_adjacent = temp
    return max_number(sum_non_adjacent, sum_adjacent)


if __name__ == '__main__':
    nums_demo1 = [5, 1, 1, 5]                   # expected 10
    nums_demo2 = [2, 4, 6, 2, 5]                # expected 13
    print(airbnb_question(nums_demo1))
    print(airbnb_question(nums_demo2))


"""
    
    +) Time complexity: O(n) với n là len(nums)-1.
    +) Space memory: O(1).

"""
