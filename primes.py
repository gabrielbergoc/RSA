def primes_list(n):
    """Returns a list with all primes smaller than or equal to n"""

    primes = [2]

    for i in range(3, n + 1, 2):
        is_prime = True

        j = 1
        while j < len(primes) and primes[j]**2 <= i and is_prime:
            if i % primes[j] == 0:
                is_prime = False

            j += 1

        if is_prime:
            primes.append(i)

    return primes
