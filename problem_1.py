one_thousand = [i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]

def sum_of(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum


print(sum_of(one_thousand))
