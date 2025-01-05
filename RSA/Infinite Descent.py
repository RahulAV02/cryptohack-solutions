from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from gmpy2 import invert

def generate_rsa_keys(bits=1024):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = invert(e, phi)
    return n, e, d

def encrypt_message(plaintext, n, e):
    m = bytes_to_long(plaintext)
    c = pow(m, e, n)
    return c

def decrypt_message(c, n, d):
    m = pow(c, d, n)
    return long_to_bytes(m)

n, e, d = generate_rsa_keys()
flag = b"crypto{?????????????????????????}"
ciphertext = encrypt_message(flag, n, e)
decrypted_message = decrypt_message(ciphertext, n, d)

print("Decrypted message:", decrypted_message)
