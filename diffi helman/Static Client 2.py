from pwn import *
from Crypto.Util.number import *
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory.residue_ntheory import discrete_log

def setup_connection():
    return remote('socket.cryptohack.org', 13378)

def receive_json():
    line = r.recvline()
    return json.loads(line.decode())

def send_json(data):
    request = json.dumps(data).encode()
    r.sendline(request)

def find_smooth_prime():
    multiplier = 1
    index = 1
    while True:
        multiplier *= index
        candidate = multiplier + 1
        if candidate.bit_length() >= p.bit_length() and isPrime(candidate):
            return candidate
        index += 1

def decrypt_with_aes(shared_secret, iv, ciphertext):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext_bytes = bytes.fromhex(ciphertext)
    iv_bytes = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
    decrypted = cipher.decrypt(ciphertext_bytes)

    if is_valid_padding(decrypted):
        return unpad(decrypted, 16).decode('ascii')
    else:
        return decrypted.decode('ascii')

def is_valid_padding(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(len(padding)))

def exploit():
    global r, p, A, iv, ciphertext

    r = setup_connection()

    r.recvuntil("Intercepted from Alice: ")
    res = receive_json()
    p = int(res["p"], 16)
    g = int(res["g"], 16)
    A = int(res["A"], 16)

    r.recvuntil("Intercepted from Bob: ")
    res = receive_json()
    B = int(res["B"], 16)

    r.recvuntil("Intercepted from Alice: ")
    res = receive_json()
    iv = res["iv"]
    ciphertext = res["encrypted"]

    smooth_prime = find_smooth_prime()
    print(f"Smooth prime bit-length: {smooth_prime.bit_length()}")

    r.recvuntil("send him some parameters: ")
    send_json({
        "p": hex(smooth_prime),
        "g": hex(2),
        "A": hex(A)
    })

    r.recvuntil("Bob says to you: ")
    res = receive_json()
    B_prime = int(res["B"], 16)

    b = discrete_log(smooth_prime, B_prime, 2)
    shared_secret = pow(A, b, p)

    flag = decrypt_with_aes(shared_secret, iv, ciphertext)
    print(f"Decrypted flag: {flag}")

    r.interactive()

if __name__ == "__main__":
    exploit()
