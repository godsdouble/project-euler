def sum_proper_divisors(n):
    if n<2:
        return None
    divisors = set({1})
    for i in range(2, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            divisors.add(i)
            divisors.add(q)
    return (n, sum(divisors))

test_for_pairs_not_prime = [sum_proper_divisors(i) for i in range(2, 10000) if sum_proper_divisors(i)[1] != 1]

amicable_pairs = set()

for i in test_for_pairs_not_prime:
    for j in test_for_pairs_not_prime:
        if i[0] == j[1] and j[0] == i[1] and i[0] != j[0]:
            amicable_pairs.add(i[0])

print(sum(amicable_pairs))

# 31626
