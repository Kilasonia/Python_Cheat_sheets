from math import *
n = int(input("Введите диапазон:-"))
p = [2, 3]
count = 2
a = 5
while (count < n):
    b = 0
    for i in range(2, a):
        if (i <= sqrt(a)):
            if (a % i == 0):
                print(a, "непростое")
                b = 1
            else:
                pass

    if (b != 1):
        print(a, "простое")
        p = p + [a]
    count = count + 1
    a = a + 2
print(p)

# Пример 