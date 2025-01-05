from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

# Generate 1600-bit RSA key components
while True:
    p = getPrime(100)  # Generate a 100-bit prime number
    q = getPrime(100)  # Generate another 100-bit prime number
    phi = (p - 1) * (q - 1)
    if GCD(e, phi) == 1:  # Ensure e and φ(n) are coprime
        d = inverse(e, phi)
        if d != -1:  # Ensure modular inverse exists
            break

n = p * q  # Calculate modulus

# Encrypt the plaintext
flag = b"YOUR_SECRET_MESSAGE"
plaintext = bytes_to_long(flag)
ciphertext = pow(plaintext, e, n)  # Encrypt using RSA formula

print(f"Public Modulus (n): {n}")
print(f"Public Exponent (e): {e}")
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
recovered_plaintext = pow(ciphertext, d, n)
decrypted_message = long_to_bytes(recovered_plaintext)
assert decrypted_message == flag

# Display decrypted result
print("Decrypted Message:", decrypted_message.decode())

# Example decryption for a fixed ciphertext
p_fixed, q_fixed = 752708788837165590355094155871, 986369682585281993933185289261
n_fixed = p_fixed * q_fixed
phi_fixed = (p_fixed - 1) * (q_fixed - 1)
d_fixed = inverse(e, phi_fixed)
ct_fixed = 39207274348578481322317340648475596807303160111338236677373
decrypted_fixed = pow(ct_fixed, d_fixed, n_fixed)
print("Decrypted Fixed Ciphertext:", long_to_bytes(decrypted_fixed).decode())
