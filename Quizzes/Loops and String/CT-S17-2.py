def ct2(x):
    y = 3
    while True:
        print(y, end=' ')
        for	z in range(1, x*y, 2):
            if (z % 3 == 1):
                print(z, end=' ');
                continue
            y += x
            if (y % 5 > 0):
                print(y, end=' ')
                break
            print(y, end=' ')
        if (y > 10): return x
        y += 1
print(ct2(7)) # print 5 values
