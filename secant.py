# Mengimport Library Numpy untuk mengelola Array Multideminsi seperti MATLAB
# Mengimport Library Math untuk menggunakan library matematika
import numpy as np
import math

# Mendefinisikan fungsi


def f(x):
    return math.exp(x)-4*x


# Mendefinisikan nilai ephsilon
err = 10**(-5)

# Memperkirakan dugaan 10 iterasi dengan nilai awal x0=1 dan x1=8
# Syarat x0!=x1
x = np.zeros(10)
x[0] = 1
x[1] = 3

# Proses Iterasi
for n in range(10):
    x[n+1] = x[n] - f(x[n])*(x[n]-x[n-1])/(f(x[n])-f(x[n-1]))
    print(n+1, '\t', x[n+1], '\t', f(x[n+1]))
    if abs(f(x[n])) < err:
        break
