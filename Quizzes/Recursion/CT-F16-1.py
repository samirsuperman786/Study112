def ct1(n, d=0):
    def	f(s, n, d): return '%s%d' % (s, 10*n+d)
    if (n <= 1): return [f('A', n, d)]
    else: return ct1(n-1, d+1) + [f('B', n, d)] + ct1(n-2, d+1)
print(ct1(3)) # prints a list of 5 strings