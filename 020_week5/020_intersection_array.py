"""
    Given 2 arrays, write a function to compute their intersection -  the intersection means the numbers
    that are in both arrays
"""


class Solution:

    @staticmethod
    def intersection(nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
