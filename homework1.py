def sum(listed, k):
    check = False
    if len(listed) == k:
        for i in listed:
            if k - i in listed:
                check = True
                break
    return check

listed = [4, 7, 1, -3, 2]
k = 5
print(sum(listed, k))