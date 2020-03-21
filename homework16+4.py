"""
    Hi, here's problem today. This problem was recently asked by Microsoft

    You have 2 integers n and m representing an n by m grid, determine the number of ways you can get
    from the top-left to the bottom-right of the matrix y going only right or down

    Example:
        n = 2, m = 2
    This should return 2, since the only possible routes are:
    Right, down
    Down, right
    Here's the signature:

    def num_ways(n, m):
        # Fill this in
    print(num_ways(2, 2))
        # 2
"""


def num_ways(n, m):
    if n == 1 or m == 1:
        return 1
    return num_ways(n-1, m) + num_ways(n, m-1)


if __name__ == '__main__':
    print(num_ways(3, 3))

"""
    +)Time complexity: O(?) em chưa xác định được 
    +)Memory space: O(1)
"""
