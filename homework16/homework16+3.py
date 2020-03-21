"""
    Hi, here's your problem today. This problem was recently asked by Google:

    There are n people lined up, and each have a height represented as an integer
    .A murder has happened right in front of them, and only people who are taller than everyone
    in front of them are ale to see what has happened. How many witnesses are there?

    def witnesses(heights):
        # Fill this in
    print(witnesses([3, 6, 3, 4, 1]))
        # 3
"""


def witnesses(heights):
    heights = heights[::-1]
    count = 1
    max_height = heights[0]
    for i in range(1, len(heights)):
        if heights[i] > max_height:
            count += 1
            max_height = heights[i]
    return count


if __name__ == '__main__':
    print(witnesses([3, 6, 3, 4, 1]))

"""
    +) Complexity time: O(n) <n: numbers of human >
    +) Memory space: O(1)
"""