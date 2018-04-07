import copy
def ct2(n):
    if (n <= 4): # note the unusual condition
        return [ [ n ] ]
    else:
        L = ct2(n//2)
        M = copy.copy(L)
        for	a in L: M += [[n] + a]
        return M
print(ct2(11))