# We know answer will be a multiple of 2520.
# We need to figure out with numbers from 11 to 20 produce a remainder
j=2520
num_check=[]

for i in range(11,21):
    if j%i!=0:
        num_check.append(i)

print (num_check)

def division1to20 (num):
    if num%11==0 and num%13==0 and num%16==0 and num%17==0 and num%19==0:
        return False
    else:
        return True

while division1to20(j):
    j+=2520
print (j)
