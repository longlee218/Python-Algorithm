"""
    A rectangle is represented as a list [x1, y1, x2, y2] where (x1, y1) are the coordinates of its bottom-left
    corner, and (x2, y2) are the coordinates of its top-right corner.

    Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only
    touch at the corner or edges do not overlap.

"""


def solution(rec1, rec2):
    if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
        return False
    elif rec1[3] <= rec2[1] or rec2[3] <= rec1[0]:
        return False
    return True


if __name__ == '__main__':
    print(solution(rec1=[1, 1, 3, 3], rec2=[1, 1, 2, 2]))

"""
    +) Time complexity: O(1)
"""