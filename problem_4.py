max_product = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        palindrome = list(str(product))
        palindrome_cond = (palindrome == palindrome[::-1])
        if palindrome_cond and product > max_product:
            max_product = product

print(max_product)

# outputs 906609-largest palindrome of a product of two 3 digit numbers
