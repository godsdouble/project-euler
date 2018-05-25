digits = list(range(1, 101))

sum_digits = (sum(digits))**2

squared = 0
for i in range(1, 101):
    squared += i**2

print(sum_digits - squared)

# outputs 25164150
