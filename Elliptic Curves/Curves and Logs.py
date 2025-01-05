import math
import hashlib
from Crypto.Util import number

O = 'Origin'

def mod_inverse(x, p):
    return pow(x, p - 2, p)

def add_curve_points(P, Q, a, p):
    if P == O:
        return Q
    if Q == O:
        return P

    if P[0] == Q[0] and P[1] == -Q[1]:
        return O

    if P != Q:
        lam = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p)
    else:
        lam = (3 * pow(P[0], 2) + a) * mod_inverse(2 * P[1], p)

    x3 = pow(lam, 2) - P[0] - Q[0]
    x3 %= p
    y3 = lam * (P[0] - x3) - P[1]
    return (int(x3), int(y3 % p))

def multiply_point(P, n, a, p):
    result = O
    point = P
    
    while n > 0:
        if n % 2 == 1:
            result = add_curve_points(result, point, a, p)
        point = add_curve_points(point, point, a, p)
        n = n // 2
    return result

a = 497
b = 1768
p = 9739

nB = 1829
QA = (815, 3190)
S = multiply_point(QA, nB, a, p)
print(S)

sha1 = hashlib.sha1()
sha1.update(str(S[0]).encode())
print(sha1.hexdigest())
