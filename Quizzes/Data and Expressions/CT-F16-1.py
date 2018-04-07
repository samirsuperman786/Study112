def ct1(x, y, z):
    print(x	** x - y/x + y * x - z)
    y += max(x,y,z) // min(x,y,z)
    z %= x
    return 100*x + 10*y + z
print(ct1(2, 3, 5))	#hint: prints 2 values

