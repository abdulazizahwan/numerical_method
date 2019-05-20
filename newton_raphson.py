# Mengimpor Library Numpy untuk mengelola Array Multideminsi seperti MATLAB
# Mengimport Library Math untuk menggunakan library matematika
import numpy as np
import math

# Mendefinisikan fungsi
def f(x):
    return math.exp(x)-4*x

# Mendefinisikan turunan fungsi
def g(x):
    return math.exp(x)-4


# Memperkirakan dugaan 10 iterasi dengan nilai awal x0=1
x = np.zeros(10)
x[0] = 1

# Proses  Iterasi
for n in range(10):
    x[n+1] = x[n]-f(x[n])/g(x[n])
    print(n, '\t', x[n], '\t', f(x[n]))
