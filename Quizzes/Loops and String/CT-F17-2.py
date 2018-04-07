def ct1(s):
    t = ""
    r = 0
    for c in s:
        if c.isdigit() and int(c)%2 == 0:
            t += c
        elif c.isalpha():
            r += 3
        elif c.isalnum():
            r += 1
        elif c.isspace():
            t = "%s%d"%(t,r)
            r = 0
        else:
            print("0", end="")
    return (t)
print(ct1("B32$ 85!e "))
