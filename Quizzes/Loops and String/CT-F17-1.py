def ct(a, b):
    while a > 0:
        for c in range(1, 9, b):
            print(a, b, c)
            a -= 2
        b += 1
ct(8, 3)
