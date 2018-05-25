print(sum(list(map(int, list(str(2**1000))))))

# orrrr

print(sum(int(x) for x in str(2**1000)))

# outputs 1366
