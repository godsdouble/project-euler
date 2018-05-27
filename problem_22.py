# by using with open I do not need to call names.close()
with open("p022_names.txt", mode="r") as names_p22:
    name_list = names_p22.read()

clean_names = ''.join(c for c in name_list if c not in '"')
sorted_names = sorted(clean_names.split(','))


def name_score(name):
    return sum([(ord(c) - 64) for c in name])


i = 1
total = 0
for name in sorted_names:
    total += name_score(name) * i
    i += 1

print(total)

# outputs 871198282
