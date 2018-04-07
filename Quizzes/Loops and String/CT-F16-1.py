def ct1(x, y):
    for z in range(y, x):
        print(42, z, end='')
    for z in range(x, y):
        if (z < y//2):
            if (z%2 == 0): print (2, z, end='')
            elif (z%5 == 0): print(5, z, end=' ')
        elif (x+y+z	== 27):
            print(27, z, end='')
    w = 0
    for z in range(x, 10*x, x):
        if (z < 5*x): continue
        elif (z >= 7*x): return w
        w += z
    return 99
print(ct1(3, 13)) # prints 7 values
