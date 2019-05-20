# Soal
# Sebuah daerah dijangkiti oleh epidemi demam berdarah.
# Misal f(t) menyatakan banyak orang yang terjangkit demam berdarah setelah t minggu
# Seorang petugas mencatat data sebagai berikut:
#   --------------------------------------
#   | t(minggu) | 1  |  2 |  4 |  5 |  7 |
#   --------------------------------------
#   |   f(t)    | 3  |  8 | 15 | 25 | 40 |
#   --------------------------------------
# Perkirakanlah jumlah penderita demam berdarah setelah 6 minggu

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
x.append(1)
x.append(2)
x.append(4)
x.append(5)
x.append(7)

y.append(3)
y.append(8)
y.append(15)
y.append(25)
y.append(40)

# for testing
xc = 6
yc = N(xc, x, y)

print('')
print('Jadi jumlah penderita demam berdarah setelah ', xc, ' minggu adalah ', yc)
# plot
t = linspace(-7, 7, 100)
u = N(t, x, y)
plot(t, u)
title('Polinom Interpolasi Newton')
plt.gcf().canvas.set_window_title('Polinom Newton Interpolasi')
grid(True)
show()
