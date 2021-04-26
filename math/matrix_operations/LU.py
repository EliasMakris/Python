from print_matrix import print_matrix
from matrix_op import matmul
from matrix_op import identity_matrix


# Decomposes a square matrix a to its factors lu: a = lu
# where l is lower and u is upper triangular, with accuracy (num. of decimals) ac
def lu_dec(a, ac):
    ac = int(ac)
    n = len(a)
    lij = identity_matrix(n)
    l = identity_matrix(n)

    # u
    for i in range(0, n-1):
        temp_lij = identity_matrix(n)

        # check if pivot is zero
        if a[i][i] == 0:
            # Permute the next rows to try to overcome the problem
            k = i+1
            while k < n-1 and a[k][i] == 0:
                k += 1
            if k == n-1 and a[k][i] == 0:
                print("\nlu_dec Warning: Singular matrix, verify matrix determinant is non-zero\n")
                return 0, a
            a[k], a[i] = a[i], a[k]

        for j in range(i+1, n):
            lij[j][i] = round((-1) * a[j][i] / a[i][i], ac)
        for k in range(n):
            temp_lij[k][i] = lij[k][i]
        a = matmul(temp_lij, a)

    # l
    for j in range(n-1, 0-1, -1):
        temp_l = identity_matrix(n)
        for i in range(n-1, j, -1):
            temp_l[i][j] = -lij[i][j]
        l = matmul(temp_l, l)

    return l, a


# Performs backward substitution to a system Ux=b where U is upper triangular
# and returns x as the solution - with accuracy (num. of decimals) ac
def back_sub(a, b, ac):
    ac = int(ac)
    n = len(b)

    # checks if a is upper triangular
    for i in range(n):
        if a[i][i] == 0:
            print("\nback_sub Warning: zero pivot located, check matrix singularity")
            print("This function only takes upper triangular matrices")
            print("Back Substitution stopped\n")
            return
        for j in range(0, i):
            if a[i][j] != 0.0 and a[i][j] != 0:
                print("\nback_sub Warning: This function only takes upper triangular matrices")
                print("Back Substitution stopped\n")
                return

    # back sub
    for i in range(n-1, 0-1, -1):
        sum1 = 0
        for j in range(i+1, n):
            sum1 += a[i][j] * b[j]
        b[i] = round((b[i] - sum1)/a[i][i], ac)
    return b


# Performs forward substitution to a system Lc=b where L is lower triangular
# and returns c as the solution - with accuracy (num. of decimals) ac
def forw_sub(a, b, ac):
    ac = int(ac)
    n = len(b)

    # checks if a is lower triangular
    for i in range(n):
        if a[i][i] == 0:
            print("\nforw_sub Warning: zero pivot located, check matrix singularity")
            print("This function only takes lower triangular matrices")
            print("Forward Substitution stopped\n")
            return
        for j in range(i+1, n):
            if a[i][j] != 0.0 and a[i][j] != 0:
                print("\nforw_sub Warning: This function only takes lower triangular matrices")
                print("Forward Substitution stopped\n")
                return

    # back sub
    for i in range(0, n):
        sum1 = 0
        for j in range(0, i):
            sum1 += a[i][j] * b[j]
        b[i] = round((b[i] - sum1)/a[i][i], ac)
    return b


# Solves ax=b using lu decomposition with accuracy (num. of decimals) ac
def lu_solve(a, b, ac):
    ac = int(ac)
    l, u = lu_dec(a, ac)
    c = forw_sub(l, b, ac)
    x = back_sub(u, c, ac)
    return x


# --------- TEST SECTION ------------------------------

# a = identity_matrix(3)
# b = [[-1, 2, 3], [-4, -5, 6.1234], [7, 10, 9]]
# print_matrix(mat_add(a, b), 5)

# l, u = lu_dec(b, 4)
# print_matrix(l, 4)
# print_matrix(u, 4)

# l1 = [[1,0,0], [1,2,0], [2,2,1]]
# print(back_sub(u, [1, 2, 3], 4))
# print(forw_sub(l, [1, 2, 4], 4))

# v = [1, 2, 3]
# print(vec_mat_mul(v,b))

a1 = [[1, 2, 3], [4, 8, 6], [7, 14, -9]]
b1 = [1, 2, 3]
sys1 = a1.copy()
for i in range(len(sys1)):
    sys1[i].append(b1[i])

print_matrix(sys1, 4)
l1, u1 = lu_dec(a1, 4)
print_matrix(u1, 4)

#print(lu_solve(a1, b1, 4))

