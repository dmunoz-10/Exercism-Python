def triplets_with_sum(number):
    triplets = []
    for i in range(10**(len(str(number)) - 2), number // 3):
        for j in range(i + 1, number // 2):
            k = number - i - j
            triplet = sorted([i, j, k])
            if is_valid_triplet(triplet, number) and triplet not in triplets:
                triplets.append(triplet)
    return triplets


def is_valid_triplet(triplet, number):
    num1, num2, num3 = triplet
    return num1**2 + num2**2 == num3**2 and num1 + num2 + num3 == number
