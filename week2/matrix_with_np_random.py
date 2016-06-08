import numpy as np
import time

print("Let's create random N*N matrix!")
n = int(input("input a number N to generate N*N matrix > "))

# assign random number to matrix a & b
matrix_a = np.random.randint(0, n * n, n * n).reshape(n, n)
matrix_b = np.random.randint(0, n * n, n * n).reshape(n, n)

begin = time.time()

matrix_c = matrix_a.dot(matrix_b)

end = time.time()

print(matrix_c)

print("time: %.6f sec" % (end - begin))

total = 0
for i in range(n):
    for j in range(n):
        total += matrix_c[i, j]

print("sum: %.6f" % total)