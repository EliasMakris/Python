from print_matrix import print_matrix
from permutation_algos import perm


# Calculates determinant of matrix a using Leibniz formula
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


# Solves ax=b using Cramer's rule
def cramer(a, b, ac):
    ac = int(ac)
    n = len(b)
    at = [list(i) for i in zip(*a)]
    deta = det_leib(a)
    if deta == 0:
        print("Determinant 0, system unsolvable")
        return
    x = [0. for _ in range(n)]
    for i in range(n):
        ati = [[] for _ in range(n)]
        for j in range(n):
            ati[j] = at[j]
        ati[i] = b
        x[i] = round(det_leib(ati)/deta, ac)
    return x


# --------- TEST SECTION ------------------------------

a = [[1, 2, 3], [4, 5, 6], [7, 8, -9]]
b = [1, 2, 3]
print_matrix(a, 4)

print(det_leib(a))
print(cramer(a, b, 4))


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
