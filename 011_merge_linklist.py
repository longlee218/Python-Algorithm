"""
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:

          Input:
          [
             1->4->5,
             1->3->4,
             2->6
          ]
          Output:
            1->1->2->3->4->4->5->6
"""

# Solution 1


def merge1(array):
    number_max = 0
    number_min = 0
    for i in range(1, len(array)):
        array[0] += array[i]
    temp = str(''.join(array[0].split('->')))
    temp = [int(i) for i in temp]

    # counting sort
    for i in temp:
        if i > number_max:
            number_max = i
        elif i < number_min:
            number_min = i
    count_array = [0 for i in range(number_max-number_min+1)]
    result = [0 for i in range(len(temp))]
    for i in range(len(temp)):
        count_array[temp[i] - number_min] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]
    for i in range(len(temp)):
        result[count_array[temp[i] - number_min] - 1] = temp[i]
        count_array[temp[i] - number_min] -= 1
    result = [str(i) for i in result]
    return '->'.join(result)

# Solution2


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '{}->{}'.format(self.value, self.next)


def sort_list(node1, node2):
    if node1 is None:
        return node2
    elif node2 is None:
        return node1
    if node1.value <= node2.value:
        result = node1
        result.next = sort_list(node1.next, node2)
    else:
        result = node2
        result.next = sort_list(node1, node2.next)
    return result


def merge2(lists, last):
    while last != 0:
        i = 0
        j = last
        while i < j:
            lists[i] = sort_list(lists[i], lists[j])
            i += 1
            j -= 1
            if i >= j:
                last = j
    return lists[0]


if __name__ == '__main__':
    input_demo = [
        '1->4->5',
        '1->3->4',
        '2->6',
    ]
    print(merge1(input_demo))

    a = Node(1)
    a.next = Node(4)
    a.next.next = Node(6)

    b = Node(1)
    b.next = Node(3)
    b.next.next = Node(4)

    c = Node(2)
    c.next = Node(5)

    d = Node(4)
    d.next = Node(5)
    d.next.next = Node(8)

    lists_linklist = [a, b, c, d]
    lasted = len(lists_linklist)-1
    print(merge2(lists_linklist, lasted))


"""
Solution1:
    +) Time complexity: O(n+m) <n: len của array, m: max_number-min_number+1>
    +) Memory space: O(n+m)
    +) Mô tả: Thuật toán đưa list các string về list các số int. 
              Tiến hành sắp xếp bằng counting sort, trả lại output như đề bài.

Solution2:
    +) Time complexity: O(nKlogK) <hàm merge2 vòng lặp thực hiện sort_list() với logK lần với K là độ dài list chứa linklists, 
                                    đệ quy n*K phần tử (n là số node của mỗi linklist)>
    +) Memory space: O(n) <n: số node của mỗi linklist>
"""