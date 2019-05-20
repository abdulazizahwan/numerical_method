from __future__ import print_function
from pylab import *


def divided_difference(x, y):
    """Compute interpolated polynomial coefficients using divided differences.

    USAGE:
        a = divided_difference( x, y )

    INPUT:
        x, y   - integer or float arrays of x and y coordinates

    OUTPUT:
        float array - array of interpolating polynomial coefficients

    NOTES:
        This function computes the divided differences that can be used to
        construct an interpolating polynomial for the given set of data.
        Given the array a returned by this function, the value of the
        interpolating polynomial (degree will be at most n) evaluated at
        r is given by:
            s = a[n]
            for i in range( n, 0, -1 ):
                s = s * ( r - x[i-1] ) + a[i-1]
    """

    nx = shape(x)
    ny = shape(y)

    if max(nx) != max(ny):
        print('both input variables must be vectors of the same length')
        return
    elif len(nx) != 1 or len(ny) != 1:
        print('both input variables must be vectors, not matrices')
        return

    n = max(nx) - 1
    a = y.copy()

    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            a[j] = float(a[j] - a[j-1]) / float(x[j] - x[j-i])

    return a


def evaluate(r, x, a):
    """Evaluate divided difference polynomial at r

    USAGE:
        a = evaluate( r, x, a )

    INPUT:
        r      - integer or float scaler or numpy array of evaluation points
        x      - integer or float array of interpolation point x coordinates
        a      - coefficient array returned by divided_difference()

    OUTPUT:
        float array - float scalar or array of y-values corresponding to r
    """

    n = len(a) - 1
    s = a[n]
    for i in range(n - 1, -1, -1):
        s = s * (r - x[i]) + a[i]
    return s
