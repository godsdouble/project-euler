primes = [2, 3]

def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(3,num,2):
            if num%i==0:
                return False
            else:
                return True


while len(primes)<=100:
    for i in range(3,10000,2):
        if is_prime(i):
            primes.append(i)

print (primes)


