def func():
    n = 600851475143
    i = 2
    while i * i < n:
         while n % i == 0:
            n = n / i
         i = i + 1
    print(n)

func()


primeFactors = []

def findPrimeFactors(n, basePrime):
    while basePrime ** 2 < n:
        if n % basePrime == 0: #Result not always a prime factor, doesn't matter.
            n = n / basePrime
            primeFactors.append(basePrime)
            primeFactors.append(n)
        else:
            basePrime += 1

findPrimeFactors(600851475143, 2)
print (primeFactors) 