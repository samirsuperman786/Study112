def	ct2(x):
    counter	=	0
    target	=	2	# does	not	start	at	0
    while	(target	<	4):
        if	((x	+	counter//2)	==	target):
            print(counter,	target,	end='	')
            target	+=	1
        counter	+=	1
    return	10*counter+target
print(ct2(2))		#	prints	5	values