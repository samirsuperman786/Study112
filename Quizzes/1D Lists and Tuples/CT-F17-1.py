def solveCt(a):
    a[1] = "foo"
    a[0], a[2] = a[2], a[0]
    print(a)
    
    b = a
    b.extend([42, "wow" ])
    b.pop()
    print(b)
    
    c = [] + b
    c[1:-1] = ["Hello" , "World" ]
    return c
    
lst = [15, "1" , "twelve" ]
print(solveCt(lst))
print(lst)
