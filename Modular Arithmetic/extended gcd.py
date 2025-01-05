def extended_gcd(a, b):
    old_r, r = a, b
    old_u, u = 1, 0
    old_v, v = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_u, u = u, old_u - quotient * u
        old_v, v = v, old_v - quotient * v

    return old_r, old_u, old_v 

if __name__ == "__main__":
    p = 26513
    q = 32321

    gcd, u, v = extended_gcd(p, q)
    print("The lower value between u and v is:", min(u, v))
