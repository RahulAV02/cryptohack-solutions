from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import math

def aes_decrypt(shared_secret, iv, ciphertext):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode())
    key = sha1.digest()[:16]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    
    try:
        return unpad(plaintext, AES.block_size).decode('utf-8')
    except ValueError:
        return plaintext.decode('utf-8')

def find_logarithm(p, g, A, B):
    max_attempts = 1000000
    for i in range(1, max_attempts):
        if pow(g, i, p) == A:
            a = i
            break
    else:
        raise Exception("Discrete log not found within attempt limit")

    shared_secret = pow(B, a, p)
    return shared_secret

def main():
    p_hex = "0xde26ab651b92a129"
    g_hex = "0x2"
    A_hex = "0x637430f37c694fa7"
    B_hex = "0x7249365a2a8c71ff"
    iv_hex = "31077c28f19c90297f3da6dff6ca3019"
    encrypted_flag_hex = "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"
    
    p = int(p_hex, 16)
    g = int(g_hex, 16)
    A = int(A_hex, 16)
    B = int(B_hex, 16)
    
    iv = bytes.fromhex(iv_hex)
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)
    
    a = 7596561454821291306
    
    secret = find_logarithm(p, g, A, B)
    
    flag = aes_decrypt(secret, iv, encrypted_flag)
    print(f"Decrypted flag: {flag}")

if __name__ == "__main__":
    main()
