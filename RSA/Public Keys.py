from Crypto.Util.number import inverse

plaintext = 12
e = 65537
p = 17
q = 23

n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

ciphertext = pow(plaintext, e, n)
decrypted = pow(ciphertext, d, n)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
