"""
multiplication function for calculate the multiplication of two input matrix
print_matrix function to print the matrix row by row
"""

# matrix z = matrix x * matrix y (for any matrix)
def multiplication1(x, y):
    z = []
    i = 0
    while i < len(x):
        j = 0
        row =[]
        while j < len(y[0]):
            k = 0
            r = 0
            while k < len(x[0]):
                r += x[i][k] * y[k][j]
                k += 1
            j += 1
            row.append(r)
        z.append(row)
        i += 1
    return(z)

    # z = []
    # for i in range(len(x)):
    #     row =[]
    #     for j in range(len(y[0])):
    #         r = 0
    #         for k in range(len(x[0])):
    #             r += x[i][k] * y[k][j]
    #         row.append(r)
    #     z.append(row)
    # return(z)


# if two matrix are n*n matrix
def multiplication2(x, y, n):
    z = []
    for item in range(n):
        z.append([0] * n)  # create a n*n matrix with all values == 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i][j] += x[i][k] * y[k][j]
    return z


def print_matrix(m):
    for row in m:
        print (row)
