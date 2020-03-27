"""
    Let's consider a word too long, if it length is strictly more than 10 characters. All too long worlds
    should be replaced with a special abbreviation.

    This abbreviation is made like this: we write down the first and the last letter of a word and between them
    we write a number of letters between the first and the last letters. That number is in decimal system and
    doesn't contain any leading zeroes.

    Thus, "localization" will spelt as "l10n" and "internationalization" as "i18n".


"""


def code():
    n = 0
    while n < 1 or n > 100:
        n = int(input("Enter n: "))
    string = []
    for i in range(n):
        string.append(input(""))
    for i in range(n):
        if len(string[i]) >= 10:
            string[i] = string[i][0] + str(len(string[i])-2) + string[i][-1]
    return "\n".join(string)


if __name__ == '__main__':
    print(code())
