def matmul(a, b):
    bt = [list(i) for i in zip(*b)]
    return [[sum(ea*eb for ea, eb in zip(colb, rowa)) for colb in bt] for rowa in a]


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [list(i) for i in zip(*A)]
Bt = [list(i) for i in zip(*B)]
AB = [[sum(ea*eb for ea, eb in zip(colb, rowa)) for colb in Bt] for rowa in A]

for row in matmul(A, B):
    print(row)
print('')

for i in range(0, len(A)):
    print(A[i])
print('')
for i in range(0, len(B)):
    print(B[i])
print('')
for i in range(0, len(AB)):
    print(AB[i])
print('')
