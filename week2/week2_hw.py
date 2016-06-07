import numpy as np
import time
import matplotlib.pyplot as plt

numbers = range(100)

for n in numbers:
    matrix_a = np.zeros((n, n))
    matrix_b = np.zeros((n, n))

    # assign values to matrix a & b follow rules
    for i in range(n):
        for j in range(n):
            matrix_a[i, j] = i * n + j
            matrix_b[i, j] = j * n + i

    begin = time.time()

    matrix_c = matrix_a.dot(matrix_b)

    end = time.time()

    running_time = (end - begin)

    x = n
    y = running_time
    plt.plot(x, y, 'o', color = 'black')

plt.title('Relationship between N and the execution time')
plt.xlabel('N')
plt.ylabel('execution running time(sec)')
plt.show()
