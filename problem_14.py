def collatz(n):
    seq.append(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        collatz(n / 2)
    else:
        collatz(3 * n + 1)


longest_chain = 0

for i in range(500001, 1000000, 2):
    seq = []
    collatz(i)
    if len(seq) > longest_chain:
        longest_chain = len(seq)
        biggest = i

print(biggest, ":", longest_chain)

# outputs 837799
