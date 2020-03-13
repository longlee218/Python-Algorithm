"""
    Hi, here's your prblem today. This problem was recently ask by Microsoft

    You are given an array of integers. Return the largest product that can be made by
    multiplying any 3 integers in the array
    Example

    [-4, -4, 2, 8] should return 128 as the largest product can made by multiplying
    -4 * -4 * 8 =128

    Here's a staring point:

    def maximum_product_of_three(lst):
        # Fill this in.
    print(maximum_product_of_three([-4, -4, 2, 8])
        # 128
"""
# Solution1


def maximum_product_of_three1(lst):
    max_number = max(lst)
    for i in range(0, len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                if max_number < lst[i]*lst[j]*lst[k]:
                    max_number = lst[i]*lst[j]*lst[k]
    return max_number

# Solution2


def maximum_product_of_three3(lst):
    min_value1 = 999999999999999
    min_value2 = min_value1
    max_value1 = -min_value1
    max_value2 = max_value1
    max_value3 = max_value1
    for i in lst:
        if i > max_value1:
            max_value3 = max_value2
            max_value2 = max_value1
            max_value1 = i
        elif i > max_value2:
            max_value3 = max_value2
            max_value2 = i
        elif i > max_value3:
            max_value3 = i
        if i < min_value1:
            min_value2 = min_value1
            min_value1 = i
        elif i < min_value2:
            min_value2 = i
    return max(min_value1*min_value2*max_value1, max_value1*max_value2*max_value3)


if __name__ == '__main__':
    array = [-4, -20, 5, -2, -4, 6]
    print(maximum_product_of_three1(array))
    print(maximum_product_of_three3(array))


"""
    Solution1:
        +)Time complexity: O(n^3) <n là len của lst>
        +)Space memory: O(1)
        +)Phân tích: nhân 3 số với nhau rồi làm như tìm max bthg
        
    Solution2:
        +)Time complexity: O(n) <n là len của lst>
        +)Space memory: O(1)
        +)Phân tích: nhận thấy nếu tích 3 số để max có 2 trường hợp: 3 số dương và 2 sô âm 1 số dương
                    Tiến hành tìm 2 số âm nhỏ nhất của chuỗi và 3 số dương lớn nhất
                    
                    [min1, min2,......... max3, max2, max1 ]
                    
                    So sánh tích của 2 trường hợp này --> min1*min2*max1 với max3*max2*max1
"""