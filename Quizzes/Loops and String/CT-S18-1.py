def ct1(s):
    a = len(s) - 1
    b = ""
    for i in range(a, 0, -2):
        b = s[i] + b
        c = int(s[i-1])
        print(s[:i:c])
    return b
print(ct1("s3a1n4d2y")) # string length: 9