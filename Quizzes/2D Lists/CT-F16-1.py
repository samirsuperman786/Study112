import copy
def	ct1(L):
    a	=	L
    b	=	copy.copy(L)
    c	=	copy.deepcopy(L)
    a[0]	=	b[1]
    b[1][1]	=	c[0]
    c[1].append(b[1])
    a[0][0]	+=	(b[1].pop())[0]
    return	(a,b,c)
#	Be	careful	to get	the	brackets	
#	and	commas	right!
for	val	in	ct1([[1],[2,5]]):
    print(val)	#	prints	3	lines
