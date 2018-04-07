def ct2(n, m=0, depth=0):
    indent = '  '*depth
    print(indent, '(%d,%d)' % (n, m))
    if (n <= 0):
        result = int(str(n)+str(m))
    else:
        result = ct2(n//2, m+1, depth+1) + ct2(n-4, m+2, depth+1)
    print(indent, '-->', result)
    return result
ct2(3)	# Note:	you must correctly indicate newlines and indents
        # Hint: prints 10 lines