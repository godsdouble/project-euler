# We know answer will be a multiple of 2520.
# We need to figure out which numbers from 11 to 20 produce a remainder
num = 2520
factors = [num]

for i in range(11, 21):
    if num % i != 0:
        factors.append(i)

while True:

    mod_num = [num % factor for factor in factors]

    # if list has a mod = 0 for each factor in this list, then set size
    # will be 1 with value 0 inside. I do not need to make a check for 0
    # because first factor is 2520 and it is being incremented by 2520,
    # so this mod will always be 0.

    if len(set(mod_num)) == 1:
        break
    num += 2520

print(num)

# outputs 232792560
