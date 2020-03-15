def is_armstrong_number(number):
    temp = []
    for i in str(number):
        temp.append(int(i)**len(str(number)))
    return sum(temp) == number
