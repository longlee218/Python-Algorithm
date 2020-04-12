"""
    Everyone knows that lucky numbers are positive whose decimal representation contains only the
    lucky digits 4 and 7. For example 47, 744 and 4 are lucky and 5, 17, 467 are not.

    Number is almost lucky if it could be evenly divided by some lucky number. Find almost lucky number.


"""


def check_almost_lucky_number():
    n = -1
    while n < 1 or n > 1000:
        n = int(input("Enter number: ").strip())
    if n % 4 == 0 or n % 7 == 0:
        return "YES"
    while n > 0:
        if n % 10 != 4 and n % 10 != 7:
            return "NO"
        n = int(n / 10)
    return "YES"


if __name__ == '__main__':
    print(check_almost_lucky_number())
