from pwn import *
import json
import os


block1 = os.urandom(32)
block2 = os.urandom(32)


m1 = block1.hex()
m2 = block2.hex()

payload = {
    "message_1": m1,
    "message_2": m2
}


with remote("socket.cryptohack.org", 13405) as r:
    r.sendlineafter(b'Provide your JSON: ', json.dumps(payload).encode())
    response = r.recvline()

print(f"Server Response: {response.decode()}")
