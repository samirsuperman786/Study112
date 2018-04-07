def ct1(L):
    result = []
    M=[L[i]*10**i for i in range(len(L))]
    for val in M:
        result.extend([val, L.pop()])
    return result
L=[2,5,3]
M=ct1(L)
print(L, M)