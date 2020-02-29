
def trans(expression):
    return list(expression.split())


def eval(expression):
    trans(expression)
    sign = 1        # lưu dấu (sign=1 dương, sign=-1 âm)
    number = []     # mảng lưu các số
    sum1 = 0        # lưu tổng giá trị các số
    result = 0      # kết quả cuối cùng
    index = 0       # chỉ số
    while index < len(expression):
        if expression[index] == '(':
            number.append(result)       # push kết quả vào mảng lưu các số
            number.append(sign)         # push 1 vào
            result = 0      # reset lai ket qua
            sign = 1        # reset dau
        elif expression[index] == ')':
            result *= number.pop()      # pop number xử lý phép nhân trước
            result += number.pop()      # pop number xử lý phép cộng
        elif expression[index] == '+':
            sign = 1
        elif expression[index] == '-':
            sign = -1
        elif expression[index].isdigit():
            sum1 += int(expression[index])
        result += sum1 * sign
        sum1 = 0                    # reset lại tổng giá trị các số
        index += 1
    return result           # kết quả cuối

# cach 2


def calculate(x, y, ops):
    if ops == '*':
        return x*y
    elif ops == '/':
        return x//y


def eval_ver2(expression):
    stack_number = []
    stack_op = []
    sign = 1
    result = 0
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            if len(stack_op) == 0:
                stack_number.append(int(expression[i])*sign)
                sign = 1
            elif stack_op[-1] == '(':
                stack_number.append(int(expression[i]) * sign)
                sign = 1
            else:
                number1 = stack_number.pop()
                number2 = int(expression[i])*sign
                stack_number.append(calculate(number1, number2, stack_op.pop()))
        elif expression[i] == '-':
            sign = -1
        elif expression[i] == '+':
            sign = 1
        else:
            stack_op.append(expression[i])
        i += 1
    return sum(stack_number)


if __name__ == '__main__':
    print(eval('-(3+(3-2)'))
    print(eval('-3*(3-2)'))
    print(eval_ver2('8/4'))
    print(eval_ver2('-2*8/4'))

