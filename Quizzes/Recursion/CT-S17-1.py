def ct1(L):
    if (L == [ ]):
        return L
    elif (L[-1] % 2	== 0):
        R =	L[::-1]
        return [ 7, max(L[:2]) ] + ct1(R[:-2])
    else:
        return ct1(L[:-2]) + [ 8, sum(L[:2]) ]
print(ct1([1,3,4,6,2,5])) # prints a list with 6 ints