# Re-did thise problem to practice Classes and Generators


class Fibonacci():

    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def nth_term(self, n=1):
        for i in range(n):
            yield self.a
            self.a, self.b = self.b, self.a + self.b


limit = 4000000  # Last Fib value must not exceed this limit
seq = Fibonacci(1, 2)
even_seq = []

# Generator will not execute 4000000 times as the running sum will reach
# it way before.
for number in seq.nth_term(limit):
    if number > limit:  # Will break out when limit is exceeded
        break
    elif number % 2 == 0:  # Store only even numbers
        even_seq.append(number)
    else:
        pass

print(sum(even_seq))

# outputs 4613732
