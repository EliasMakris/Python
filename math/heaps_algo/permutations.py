def perm(n, a):
    if n == 1: yield a
    else:
        for i in range(n - 1):
            for hp in perm(n - 1, a): yield hp
            j = 0 if (n % 2) == 1 else i
            a[j], a[n - 1] = a[n - 1], a[j]
        for hp in perm(n - 1, a): yield hp


b = [1, 2, 3]
for i in perm(3, b):
    print(i)
