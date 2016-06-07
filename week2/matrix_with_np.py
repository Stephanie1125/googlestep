import numpy as np
import time

print("Let's create N*N matrix with built in rules!")
n = input("input a number N to generate N*N matrix > ")

matrix_a = np.zeros((n, n))
matrix_b = np.zeros((n, n))
matrix_c = np.zeros((n, n))

# assign values to matrix a & b follow rules
for i in range(n):
    for j in range(n):
        matrix_a[i, j] = i * n + j
        matrix_b[i, j] = j * n + i
        matrix_c[i, j] = 0

begin = time.time()

matrix_c = matrix_a.dot(matrix_b)

end = time.time()

print(matrix_c)

print "time: %.6f sec" % (end - begin)

total = 0
for i in range(n):
    for j in range(n):
        total += matrix_c[i, j]

print "sum: %.6f" % total

