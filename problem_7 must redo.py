import math


def generate_prime(nth_prime):
    # using Prime Number Theorem (PNT) and overestimating by factor of 2
    estimated_num_of_prime = int(2 * nth_prime * math.log(nth_prime))
    prime = [True] * estimated_num_of_prime
    count = 0

    for i in range(2, estimated_num_of_prime):
        if prime[i]:
            count += 1
        if count == nth_prime:
            return i
        for j in range(i * 2, estimated_num_of_prime, i):
            prime[j] = False


print(generate_prime(10001))

# outputs 104743
