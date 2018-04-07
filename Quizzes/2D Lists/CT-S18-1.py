import copy
def ct5(a):
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a = a + [ 10 ]
    b[1][0] = "one"
    c[0] = "two"
    d[0].extend(d[1])
    d[1][1] = 12
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
e = [ [ 2, 4 ], [ 6, 8 ] ]
ct5(e)
print("e:", e)
