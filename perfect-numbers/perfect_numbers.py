def classify(number):
    if number < 1:
        raise ValueError('Invalid number, only positive numbers')

    numbers = range(1, (number + 1 // 2))
    aliquot_sum = sum(filter(lambda n: (number % n) == 0, numbers))
    if aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'perfect'
