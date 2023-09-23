a = 6
i = 1
perfect = 0
while a > 0:
    if a % i == 0:
        perfect = perfect + i
a = a - 1
i = i + 1
print(perfect)
if perfect == a:
    print(perfect, " is perfect number")
else:
    print(perfect, "is not perfect")
