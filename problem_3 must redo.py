import math

n = 600851475143  # Find largest prime factor of this number
limit = int(math.sqrt(n)) + 1
prime_factors = []


# Using Sieve of Eratosthenes
def generate_primes(up_to_this_num):
    limit = up_to_this_num + 1
    not_prime = set()

    for i in range(2, limit):
        if i in not_prime:
            continue

        for j in range(i * 2, limit, i):
            not_prime.add(j)

        yield i


for prime in generate_primes(limit):
    if n % prime == 0:
        prime_factors.append(prime)

print(prime_factors)
print(max(prime_factors))

# output is 6857
