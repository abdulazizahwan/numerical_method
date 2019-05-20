# Soal
# Misal f(t) menyatakan banyaknya bakteri yang berkembang biak setelah t detik.
# Seorang petugas mencatat data sebagai berikut:
#   ---------------------------------------------------------------------
#   | t(detik)  |  0.1  |  0.3  |  0.5  |  0.7  |  0.9  |  1.1  |  1.3  |
#   ---------------------------------------------------------------------
#   |   f(t)    | 0.003 | 0.067 | 0.148 | 0.248 | 0.370 | 0.518 | 0.697 |
#   ---------------------------------------------------------------------
# Gunakan metode Polinom Newton Gregory Maju untuk menaksir banyaknya bakteri untuk t=1.2 detik


# calculating u mentioned in the formula
def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

# calculating factorial of given number n


def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# Driver Code
# Number of values given
n = 7
x = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3]

# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 0.003
y[1][0] = 0.067
y[2][0] = 0.148
y[3][0] = 0.248
y[4][0] = 0.370
y[5][0] = 0.518
y[6][0] = 0.697

# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print(" ")

# Value to interpolate at
value = 1.2

# initializing u and sum
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)

print("\nJadi banyaknya bakteri saat t =", value,
      "adalah", round(sum, 10))

# This code is contributed by mits
