def is_armstrong_number(number):
    temp = [int(i)**len(str(number)) for i in str(number)]
    return sum(temp) == number
