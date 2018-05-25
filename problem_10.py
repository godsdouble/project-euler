# Prime generator from problem 3
def generate_primes(up_to_this_num):
    limit = up_to_this_num + 1
    not_prime = set()

    for i in range(2, limit):
        if i in not_prime:
            continue

        for j in range(i * 2, limit, i):
            not_prime.add(j)

        yield i


sum = 0
for prime in generate_primes(2000000):
    sum += prime

print(sum)

# outputs 142913828922
