import copy
def ct1(a):
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)
    c[0] = [5, 6]
    b[0][1] = "two"
    c[1][0] = "twenty"
    c[0][0] = 9
    d[1] = [7, 8]
    c[1].insert(0, c[1].pop())
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

z = [ [1, 2], [3, 4] ]
ct1(z)
print("z =", z)