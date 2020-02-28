
def trans(expression):
    return list(expression.split())


def eval(expression):
    trans(expression)
    sign = 1
    number = []
    sum1 = 0
    result = 0
    for index in range(len(expression)):
        if expression[index] == '(':
            number.append(result)
            number.append(sign)
            result = 0      # reset lai ket qua
            sign = 1        # reset dau
        elif expression[index] == ')':
            result *= number.pop()
            result += number.pop()
        elif expression[index] == '+':
            sign = 1
        elif expression[index] == '-':
            sign = -1
        if expression[index].isdigit():
            sum1 += int(expression[index])
        result += sum1 * sign
        sum1 = 0
    return result + sum1 * sign


if __name__ == '__main__':
    express = '-(3+(3-2))'
    print(eval(express))
