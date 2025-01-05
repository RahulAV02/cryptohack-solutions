import math
from decrypt_08c0fede9185868aba4a6ae21aca0148 import decrypt_flag

O = 'Origin'

def inv_mod(x, p):
    return pow(x, p-2, p)

def ecc_points_add(P, Q, a, p):
    """ Add two points on the elliptic curve """
    if P == O:
        return Q
    if Q == O:
        return P

    if P[0] == Q[0] and P[1] == -Q[1]:
        return O

    if P != Q:
        lam = (Q[1] - P[1]) * inv_mod(Q[0] - P[0], p)
    else:
        lam = (3 * pow(P[0], 2) + a) * inv_mod(2 * P[1], p)

    x3 = pow(lam, 2) - P[0] - Q[0]
    x3 %= p
    y3 = lam * (P[0] - x3) - P[1]
    return (int(x3), int(y3 % p))

def scalar_mul(P, n, a, p):
    """ Multiply a point P by scalar n on the elliptic curve """
    R = O
    Q = P
    while n > 0:
        if n % 2 == 1:
            R = ecc_points_add(R, Q, a, p)
        Q = ecc_points_add(Q, Q, a, p)
        n = n // 2
    return R

def sqrt(x, q):
    """ Find the square root modulo q """
    for i in range(1, q):
        if pow(i, 2) % q == x:
            return (i, q - i)
    return None

if __name__ == '__main__': 
    a = 497
    b = 1768
    p = 9739
 
    q_x = 4726
    nB = 6534
    iv = 'cd9da9f1c60925922377ea952afc212c'
    encrypted_flag = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'
 
    y1, y2 = sqrt((pow(q_x, 3) + a * q_x + b) % p, p)

    Q1 = (q_x, int(y1))
    Q2 = (q_x, int(y2))


    if Q1[1] % 4 == 3:
        secret = scalar_mul(Q1, nB, a, p)
    else:
        secret = scalar_mul(Q2, nB, a, p)


    flag = decrypt_flag(secret[0], iv, encrypted_flag)
    print(flag)
