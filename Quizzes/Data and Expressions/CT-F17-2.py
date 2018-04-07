def func1(x, y, z):
    print(x)
    return x//y + z
def func2(x, y, z):
    print(y)
    return func1(y*2,x+2,z-3)
def func3(x, y, z):
    print(z)
    return func2(z+5,x+3,y+2)
    
print(func3(7,4,2))
# Hint: Prints 4 value