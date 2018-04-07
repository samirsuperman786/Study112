def	ct1(A,	B,	C,	D,	E):
    result	=	[	]
                #  0	1	  2		3	   4	5	  6		7	  8		9
    pairs	=	[(A,B),(A,C),(A,D),(A,E),(B,C),(B,D),(B,E),(C,D),(C,E),(D,E)]
    for	i,pair	in	enumerate(pairs):
        (L,	M)	= pair
        if	(L	is	M):	result.append(i)
        elif	(L	==	M):	result.append(10*i)
    return	result
def	f(L):
    L[0]	+=	1
    return	L
A	=	list(range(3))
B	=	copy.copy(A)
C,	D,	E	=	A,	B+[	],	f(B)
print(ct1(A, B, C, D, E))