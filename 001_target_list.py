"""
    This problem was asked by Facebook:

    You are given a list of numbers, and a target number k. Return whether of not there are 2 nubmers
    in the list that add up to k.

    Example:
        Given a list =  [4, 7, 1, -3, 2] and k =5

        def two_sum(list, k):
            # Fill this

        print two_sum(list, 5)

"""


def two_sum1(listed, k):
    check = False
    for i in listed:
        if k - i in listed:
            check = True
    return check


def two_sum2(listed, k):
    for i in range(len(listed)):
        current = listed[i]
        for j in range(i+1, len(listed)):
            if current + listed[j] == k:
                return True
    else:
        return False


if __name__ == "__main__":
    array = [4, 7, 1, -3, 2]
    key = 5
    print(two_sum1(array, key))
    print(two_sum2(array, key))
