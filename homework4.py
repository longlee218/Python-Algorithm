
def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    array = [4, 3, 2, 4, 1, 3, 2]
    print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
