#the following was a useless attempt to generate three digit numbers without using range function lol
"""
digits = list(range(0,10))

three_digits_listed = list(itertools.product(digits, repeat=3))

print(three_digits_listed[999])

digits_to_999=[]

for i in range (0,1000):
    joining = (str(three_digits_listed[i][0]), str(three_digits_listed[i][1]), str(three_digits_listed[i][2]))
    digits_to_999.append(int("".join(joining)))

print (digits_to_999)
"""
import itertools

def isPalindrome(elem):
    d = str(elem)
    rev_d = reversed(d)
    if list(d)==list(rev_d):
        return True
    else:
        return False

digits_to_999 = list(range(100,1000))

test_product = list(itertools.combinations_with_replacement(digits_to_999, 2))

palindrome_list = []

for i in range(len(test_product)):
    if isPalindrome(test_product[i][0]*test_product[i][1]):
        a=test_product[i][0]*test_product[i][1]
        palindrome_list.append(a)

print (max(palindrome_list))
