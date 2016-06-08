import numpy, sys, time

# input number of N from keyboard
if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n))
b = numpy.zeros((n, n))
c = numpy.zeros((n, n))

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0

begin = time.time()

c = numpy.dot(a, b)

end = time.time()

print(c)

print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.

total = 0
for i in range(n):
    for j in range(n):
        total += c[i, j]

# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.

print("sum: %.6f" % total)