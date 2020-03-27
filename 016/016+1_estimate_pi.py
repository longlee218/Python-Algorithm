"""
    This problem was asked by Google.
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
    Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random


def estimate_pi(n):
    number_point_circle = 0
    number_point_square = 0
    for _ in range(n):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        if x1**2 + y1**2 <= 1:
            number_point_circle += 1
        number_point_square += 1
    return 4*(number_point_circle/number_point_square)


if __name__ == '__main__':
    print(estimate_pi(10000))


"""
    +) Time complexity: O(n) n là số các điểm
    +) Memory space: O(1)
"""
