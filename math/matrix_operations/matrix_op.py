# Returns the matrix product of ab
def matmul(a, b):
    bt = [list(i) for i in zip(*b)]
    return [[sum(ea*eb for ea, eb in zip(colb, rowa)) for colb in bt] for rowa in a]


# Returns the vector - matrix product va
def vec_mat_mul(v, a):
    at = [list(i) for i in zip(*a)]
    return [sum(ev*ea for ev, ea in zip(v, rowat)) for rowat in at]


# Adds matrices a and b
def mat_add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


# Returns the identity matrix of size n
def identity_matrix(n):
    a = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    return a


# Returns the "elementary" matrix "e", which if multiplied with "a" form the left: e*a,
# results to adding row "indj" to row "indi", "lij" times (square matrices of size n)
# Not used until now
def elementary_matrix(n, indi, indj, lij):
    e = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == indi and j == indj:
                e[i][j] = lij
    return e
