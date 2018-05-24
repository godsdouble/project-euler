import time
start_time = time.time()

def how_many(num):    
    result = set() # using a set removes any duplicate factors
    for i in range(1, int(num ** 0.5) + 1): # only need to check until sqrt of number
        div, mod = divmod(num, i) # great function which returns quotient AND remainder
        if mod == 0:
            result |= {i, div} # new set with elements from both s and t
    return len(result)

def triangle_num(j):
    sum=0
    while True:
        sum+=j
        yield sum
        j+=1

for el in triangle_num(1):
    if how_many(el)>500:
        print (el, how_many(el))
        print ("Done.")
        break

print("--- %s seconds ---" % (time.time() - start_time))