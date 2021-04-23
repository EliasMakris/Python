def perm(n, a):
    if n == 1: yield a
    else:
        for i in range(n - 1):
            for hp in perm(n - 1, a): yield hp
            j = 0 if (n % 2) == 1 else i
            a[j], a[n - 1] = a[n - 1], a[j]
        for hp in perm(n - 1, a): yield hp


def det_leib(a):
    n = len(a)
    sum1 = 0
    term = 0
    cnt = 0
    indices = [*range(n)]
    for p in perm(n, indices):
        for i in range(0, n):
            if i == 0:
                if cnt % 2 == 0:
                    sign = 1
                else:
                    sign = -1
                term = sign * a[0][p[0]]
            else:
                term *= a[i][p[i]]
        sum1 += term
        cnt += 1
    return sum1


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sample matrix a has det 0

# b = open("a.txt", "r").read()

'''
# Matrix as input from console
x=[]
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    x.append(row)
print(x)
'''

print(det_leib(a))
