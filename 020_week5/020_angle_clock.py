"""
    Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock

"""


def calAngle(hour, minutes):
    if hour == 12 or hour == 00:
        hour = 0
    if hour > 12:
        hour = hour - 12
    if minutes == 60 or minutes == 00:
        minutes = 0
    hour_angle = hour*30 + (minutes/60)*30
    min_angle = (minutes/60)*360
    angle = abs(hour_angle-min_angle)
    if angle > 180:
        return round(360 - angle, 2)
    return round(angle, 2)


if __name__ == '__main__':
    print(calAngle(13, 1))

"""
    +) Time complexity: O(1)
"""