def split_number_digits(number):
    hundred = number // 100
    ten = number // 10 - hundred * 10
    one = number - hundred * 100 - ten * 10
    return (str(hundred), str(ten), str(one))


num_list = [None]
string_list = []
num_dict_one = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
num_dict_tenone = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
num_dict_ten = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

for i in range(1, 1000):
    num_list.append(split_number_digits(i))

print(num_list)

for i in range(1, 1000):
    if num_list[i][0] != '0' and \
            num_list[i][1] == '0' and \
            num_list[i][2] == '0':
        string_list.append(num_dict_one[num_list[i][0]] + "hundred")
    elif num_list[i][0] != '0':
        string_list.append(num_dict_one[num_list[i][0]] + "hundred" + "and")
    if num_list[i][1] != '0' and num_list[i][1] != '1':
        string_list.append(num_dict_ten[num_list[i][1]])
    elif num_list[i][1] == '1':
        tenone = num_list[i][1] + num_list[i][2]
        string_list.append(num_dict_tenone[tenone])
        continue
    if num_list[i][2] != '0':
        string_list.append(num_dict_one[num_list[i][2]])

long_string = ''.join(string_list) + "onethousand"

print(long_string)
print(len(long_string))

# outputs 21124 characters
