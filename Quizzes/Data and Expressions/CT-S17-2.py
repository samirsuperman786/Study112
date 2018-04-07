def	f(x):	return	2*x-1
def	g(x):	return	max(x%10,	x//10%10)
def	h(x):	
    if	(x	>	0):	return	x	+	g(f(x))
    else:	return	f(min(3,	g(abs(x))))
def	ct2(x):
    print(h(x-5))
    print(h(x+5))
print(ct2(3))	#	hint:	prints	3	values