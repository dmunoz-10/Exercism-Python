def sum_of_multiples(limit, multiples):
    primes = []
    for number in range(1, limit):
        for multiple in multiples:
            if multiple != 0 and number % multiple == 0:
                primes.append(number)
                break

    return sum(primes)
