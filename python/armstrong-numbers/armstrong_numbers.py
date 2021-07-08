def is_armstrong_number(number):
    n = len(str(number))
    add = 0
    for i in str(number):
        add += int(i)**n

    return add == number