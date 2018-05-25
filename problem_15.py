# Look into Pascal's triangle / binomial expansion for other ways to solve

import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


grid_size = 20

print(nCr(grid_size * 2, grid_size))

# outputs 137846528820
