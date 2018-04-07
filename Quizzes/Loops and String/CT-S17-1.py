def ct1(x, y, z):
    count = 0
    while (x > y):
        x //= 2
        y -= z
        z += 1
        print(x, end=' ')
        print(y, end=' ')
    return z
print(ct1(20, 10, 2)) # prints 5 values