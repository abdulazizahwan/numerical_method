# Soal
# Tabel Harga Bordiran dari Tahun ke Tahun
# Misal f(x) menyatakan harga bordiran
#   ---------------------------------------------------
#   |     X     | 0.10  |  0.15 | 0.20 | 0.25 |  0.3 |
#   ---------------------------------------------------
#   |   f(X)    | 2500  |  3000 | 3700 | 4800 | 6800 |
#   ---------------------------------------------------
# Akan diuji pada x=0.22

from pylab import *


def n(j, xc, x):
    n = 1
    for i in arange(j):
        n *= (xc-x[i])

    return n


def a(j, l, x, y):
    if j == 0:
        return y[0]
    elif j-l == 1:
        return (y[j]-y[l])/(x[j]-x[l])
    else:
        return (a(j, l+1, x, y)-a(j-1, l, x, y))/(x[j]-x[l])


def N(xc, x, y):
    N = 0
    for j in range(len(x)):
        N += a(j, 0, x, y)*n(j, xc, x)
    return N


x = []
y = []
# initial value
x.append(0.10)
x.append(0.15)
x.append(0.20)
x.append(0.25)
x.append(0.30)

y.append(2500)
y.append(3000)
y.append(3700)
y.append(4800)
y.append(6800)

# for testing
xc = 0.22
yc = N(xc, x, y)

print('')
print('Jadi harga optimal bordiran pada ', xc, ' adalah ', yc)
# plot
t = linspace(-7, 7, 100)
u = N(t, x, y)
plot(t, u)
title('Polinom Interpolasi Newton')
plt.gcf().canvas.set_window_title('Polinom Newton Interpolasi')
grid(True)
show()
