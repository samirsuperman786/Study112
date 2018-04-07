def ct1(x, y, z):
    print(x/y + x//y + int(x/y))
    print(y**z + y%z)
    a = int(x) / int(y)
    return isinstance(a, int)
    
print(ct1(6, 4, 3))
# Hint: Prints 3 values