def ct4(a):
    a[2] = "olympic"
    a[0], a[2] = a[2], a[0]
    print(" ".join(a))
    b = a
    b.insert(1, "games")
    b.pop()
    print(" ".join(b))
    c = b + []
    c = c[:-1] + ["are", "here"]
    return c
lst = ["2018", "!", "woo"]
print(" ".join(ct4(lst)))
print(" ".join(lst))
