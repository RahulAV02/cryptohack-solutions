import json
from pwn import remote
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def validate_padding(data):
    length = data[-1]
    return all(byte == length for byte in data[-length:])

connection = remote('socket.cryptohack.org', 13373, level='debug')


connection.recvuntil(b'Intercepted from Alice: ')
alice_data = json.loads(connection.recvline())
prime = int(alice_data['p'], 16)
generator = int(alice_data['g'], 16)
alice_public = int(alice_data['A'], 16)


connection.recvuntil(b'Intercepted from Bob: ')
bob_public = int(json.loads(connection.recvline())['B'], 16)


connection.recvuntil(b'Intercepted from Alice: ')
encrypted_data = json.loads(connection.recvline())
iv = bytes.fromhex(encrypted_data['iv'])
encrypted_flag = bytes.fromhex(encrypted_data['encrypted'])


payload = {
    "p": hex(prime),
    "g": hex(generator),
    "A": "0x1"
}
connection.sendline(json.dumps(payload))


connection.recvuntil(b'Bob says to you: ')
shared_key = int(json.loads(connection.recvline())['B'], 16)


def decrypt_message(shared_key, iv, encrypted_flag):
    hash_obj = hashlib.sha1()
    hash_obj.update(str(shared_key).encode())
    derived_key = hash_obj.digest()[:16]

    cipher = AES.new(derived_key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_flag)

    if validate_padding(decrypted_data):
        return unpad(decrypted_data, 16).decode()
    return decrypted_data.decode()

flag = decrypt_message(shared_key, iv, encrypted_flag)
print(flag)
