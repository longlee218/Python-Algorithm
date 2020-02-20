# cach 1
def sum(listed, k):
    check = False
    if len(listed) == k:
        for i in listed:
            if k - i in listed:
                check = True
    return check

# cach 2
def two_sum(listed, k):
    if len(listed) == k:
        for i in range(len(listed)):
            current = listed[i]
            for j in range(i+1, len(listed)):
                if current + listed[j] == k:
                    return True
    else:
        return False

if __name__ == "__main__":
    listed = [4, 7, 1, -3, 2]
    k = 5
    print(sum(listed, k))
    print(two_sum(listed, k))