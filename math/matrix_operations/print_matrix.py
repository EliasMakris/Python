# Prints matrix "a" using max string length of a's elements, keeping the same length for each element
# with accuracy (num. of decimals) ac
def print_matrix(a, ac):
    ac = int(ac)
    candidates = []
    a_pos = [[len(str(round(a[i][j], ac))) for j in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(a_pos)):
        candidates.append(max(a_pos[i]))
    max_len = max(candidates)

    for i in range(len(a)):
        for j in range(len(a[0])):
            if abs(a[i][j]) < 0.1 ** (ac-1):
                a[i][j] = 0.0
            if a[i][j] < 0:
                blank_of_ele = ''
                for _ in range(max_len - len(str(a[i][j])) + 2):
                    blank_of_ele += ' '
                print(round(a[i][j], ac), end=blank_of_ele)
            else:
                blank_of_ele = ''
                for _ in range(max_len - len(str(a[i][j])) + 1):
                    blank_of_ele += ' '
                print(' ', end='')
                print(round(a[i][j], ac), end=blank_of_ele)
        print('')
    print('')


# --------- TEST SECTION ------------------------------

# a = [[-1, 2, 3], [-4, -5, 6.1234], [7, 10, 9]]
# print_matrix(a, 3)
