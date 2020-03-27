"""
    Vasily has a candles. When Vasily light up a new light up candles,
    it first burns for an hour and then it goes out.
    Vasily is smart, so he can make b went out candles into a new candles.
    As a result, this new candle can be used like any other new candle.

    Now Vasily wonder: for how many hours can his candles light up the room if he acts
    optimally well? Help him find this number?

"""


def hours_light(a, b):
    hours = 0
    while a > 0:
        a -= 1
        hours += 1
        if hours % b == 0:
            a += 1
    return hours


if __name__ == '__main__':
    print(hours_light(10, 2))
