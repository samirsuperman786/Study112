def	ct2(s):
    r	=	t	=	''
    for	i	in	range(len(s)):
        if	(s[i]	in	s[i+1:]):	r	+=	str(i)
        else:	t	+=	s[i]
    return	r	+	t[::-1]
print(ct2('aebacab'))