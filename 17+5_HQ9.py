"""
    HQ9+ is a joke programming language which has only four one-character instructions:

    "H" prints "Hello, World!",
    "Q" prints the source code of the program itself,
    "9" prints the lyrics of "99 Bottles of Beer" song,
    "+" increments the value stored in the internal accumulator.

    Instructions "H" and "Q" are case-sensitive and must be uppercase. The characters of the program which are not
    instructions are ignored.

    You are given a program written in HQ9+. You have to figure out whether executing this program will produce any output.
Input

    The input will consist of a single line p which will give a program in HQ9+. String p will contain between 1 and 100
characters, inclusive. ASCII-code of each character of p will be between 33 (exclamation mark) and 126 (tilde), inclusive.

Output
    Output "YES", if executing the program will produce any output, and "NO" otherwise.

"""


def function_H():
    print("Hello World!")


def function_Q():
    with open(__file__) as f:
        print('\n'.join(f.read().split('\n')[1:]))


def function_9():
    i = 99
    while i != -1:
        if i == 0:
            print("No more bottles of beer on the wall, no more bottles of beer.\
Go to the store and buy some more, 99 bottles of beer on the wall.\n")
        elif i == 1:
            print("{} bottle of beer on the wall, {} bottle of beer.\
Take one down and pass it around, no more bottles of beer on the wall.\n".format(i, i))
        else:
            print("{} bottles of beer on the wall, {} bottles of beer.\
Take one down and pass it around, {} bottles of beer on the wall.\n".format(i, i, i - 1))
        i -= 1


def function_plus(accumulator):
    accumulator += 1
    print(accumulator)


def function():
    command = str(input("ENTER: "))
    accumulator = 0
    if len(command) > 1 and ("H" in command or "Q" in command or "9" in command or "+" in command):
        print("YES")
    elif len(command) == 1:
        if command == "H":
            function_H()
        elif command == "Q":
            function_Q()
        elif command[0] == "9":
            function_9()
        elif command == "+":
            function_plus(accumulator)
    else:
        print("NO")


if __name__ == '__main__':
    function()
