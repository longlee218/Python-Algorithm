"""
    Hi here's your problem today. This problem was recently asked by Facebook:
    Given a list, find the k-th largest element in the list.

    Input: list = [3, 5, 2, 4, 6, 8] , k=3
    Output: 5

    Here is a staring point:

    def findKthLargest(nums, k):
        # Fill this in
    print findKthLargest([3, 5, 2, 4, 6, 8], 3)
        # 5
"""


def findKthLargest(nums, k):
    count1 = 0
    n = max(nums)
    result = [0 for i in range(n)]
    for i in range(len(nums)):
        result[nums[i]-1] = 1
    for i in range(n):
        if result[i] == 1:
            count1 += 1
        if count1 == len(nums)-k+1:
            return i+1


if __name__ == '__main__':
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))

"""
    +) Time complexity: O(n+2m) => O(n+m) <n: max number  in nums, m:len of nums> 
    +) Memory space: O(n)
"""