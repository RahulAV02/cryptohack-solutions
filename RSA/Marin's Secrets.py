from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from gmpy2 import invert

def generate_rsa_keys(bits=1024):
    a = getPrime(bits)
    b = getPrime(bits)
    n = a * b
    phi = (a - 1) * (b - 1)
    e = 65537
    d = invert(e, phi)
    return n, e, d

def encrypt_message(plaintext, n, e):
    r = bytes_to_long(plaintext)
    c = pow(r, e, n)
    return c

def decrypt_message(c, n, d):
    m = pow(c, d, n)
    return long_to_bytes(m)



n, e, d = generate_rsa_keys()


flag = b"crypto{?????????????????????????}"


ciphertext = encrypt_message(flag, n, e) 
decrypted_message = decrypt_message(ciphertext, n, d)


print("Decrypted message:", decrypted_message)
