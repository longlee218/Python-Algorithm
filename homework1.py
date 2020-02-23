
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
