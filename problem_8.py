# My logic was to reduce iterations by finding all 0 positions and
# avoiding those multiplications


def find(s, ch):
    return [i for i, char in enumerate(s) if char == ch]


def ignore_index(lst):
    for el in lst:
        lower = el - 12
        for i in range(lower, el + 1):
            ignored.add(i)


# original 1000 digit number given by Project Euler
long_string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

list_string = list(long_string)  # needed to convert into integer list

# list that will be used in a function to determine product of 13 consecutive digits
int_list = [int(el) for el in list_string]

# used to generate all 0 positions in given 1000 digits number
zero_index = find(long_string, "0")

ignored = set()  # this is updated by calling ignore_index function

# all indices to be ignored due to multiplication by 0
ignore_index(zero_index)

# using this set of all numbers from 1 to 1000 and removing all indices
# we should ignore
try_index = set(range(0, 1000))

# this set contains the indices I will try to find the largest product from
try_index.difference_update(ignored)

biggest_product = 1

for elem in try_index:
    current_product = 1
    for i in range(elem, elem + 13):
        current_product *= int_list[i]
    if current_product > biggest_product:
        start = elem  # this is the digit position where to start multiplication for the biggest product
        biggest_product = current_product

print(start, ":", biggest_product)

# outputs: 23514624000
