def fib(limit):
    a, b = 1, 2
    fib_seq=[1]
    while b<=limit:
        fib_seq.append(b)
        a, b = b, a+b
    return fib_seq

def even_list(lst):
    even = [i for i in lst if i%2==0]
    return even

def sum_of(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum

fib_sequence = fib(4000000)
fib_even = even_list(fib_sequence)
sum_is = sum_of(fib_even)
print (sum_is)