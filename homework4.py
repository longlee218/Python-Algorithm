
def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)


# def single_number(nums):
#     for i in nums:
#         if nums.count(i) == 1:
#             return i
#         else:
#             continue


if __name__ == '__main__':
    array = [4, 3, 2, 4, 1, 3, 2]
    print(singleNumber(array))
