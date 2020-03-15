def square_of_sum(number):
    if number == 1:
        return 1
    # Gauss Trick
    result = (number + 1) * number / 2
    return result**2


def sum_of_squares(number):
    if number == 1:
        return 1
    # Pyramidal Numbers
    result = number**3/3 + number**2/2 + number/6
    return result


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
