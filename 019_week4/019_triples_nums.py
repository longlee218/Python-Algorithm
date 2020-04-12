"""
    Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, c )
    in nums such that a +b +c = 0. Not that there may not be any triplets that sum to zero in nums
    and that the triplets must not be duplicates.

"""


class Solution:

    @staticmethod
    def threeSum(nums):
        triples = set()
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[i]) in triples:
                    result.append([nums[i], nums[j], -(nums[i]+nums[i])])
                print(nums[j])
                triples.add(nums[j])
        return triples


if __name__ == '__main__':
    nums = [1, -2, 1, 0, 5]
    nums2 = [0, -1, 2, -3, 1]
    print(Solution().threeSum(nums2))

"""
    +) Time complexity: O(n)
"""