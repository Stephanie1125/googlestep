"""
multiplication function for calculate the multiplication of two input matrix
print_matrix function to print the matrix row by row
"""

# matrix z = matrix x * matrix y
def multiplication(x, y):
    z = []
    i = 0
    while i < len(x):
        j = 0
        e =[]
        while j < len(y[0]):
            k = 0
            r = 0
            while k < len(x[0]):
                r += x[i][k] * y[k][j]
                k += 1
            j += 1
            e.append(r)
        z.append(e)
        i += 1
    return(z)


def print_matrix(m):
    for row in m:
        print (row)
