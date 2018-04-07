def ct2(x):
    a = 1
    while x > 1:
        print("Round %d, %0.1f" % (a, x))
        a += 1
        newX = (x ** 2) % 10
        if x == newX:
            print("boom!")
            break
        x = newX
    return x
ct2(8)