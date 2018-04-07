x = 5
def ct1(x):
    print(x % 3, x // 3)
    x = x // 10
    print(x % 7, x // 7)
    return x // 10
print(ct1(123), end=" + ")
print(x)