
def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)

# solution 2

def singleNumber2(nums):
    array1 = []
    array2 = []
    for i in nums:
        if i not in array1:
            array1.append(i)
        array2.append(i)
    return (set(array1).difference(set(array2))).pop()


if __name__ == '__main__':
    print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
    # print(singleNumber2([4, 3, 2, 4, 1, 3, 2]))
