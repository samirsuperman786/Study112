def	ct1(L):
    a	=	L
    b	=	copy.copy(L)
    c	=	copy.deepcopy(L)
    b[0]	=	a[1]	*	a[1][0]
    a[0][0]	+=	a.pop()[0]
    b[1]	=	c[0]
    return	b
#	Be careful	to	get	the	brackets and	commas	right!
L	=	[[1],[2],[3]]
print(ct1(L))
print(L)