import socket
import json
import hashlib
from Crypto.Cipher import AES

SERVER_HOST = "socket.cryptohack.org"
SERVER_PORT = 13371

def connect_to_server(host, port):
    sock = socket.create_connection((host, port))
    return sock

def send_and_receive(sock, message):
    
    sock.sendall((message + "\n").encode())
    response = sock.recv(4096).decode().strip()
    return json.loads(response)

def decrypt_flag(iv_hex, encrypted_flag_hex):
    
    iv = bytes.fromhex(iv_hex)
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)


    shared_secret = 0
    sha1_hash = hashlib.sha1(str(shared_secret).encode()).digest()
    key = sha1_hash[:16]


    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_flag)
    return decrypted

def perform_attack():
    with connect_to_server(SERVER_HOST, SERVER_PORT) as sock:
        
        response = send_and_receive(sock, "")
        prime = int(response['p'], 16)
        generator = int(response['g'], 16)
        public_key_a = int(response['A'], 16)


        manipulated_payload = json.dumps({
            "p": hex(prime),
            "g": hex(generator),
            "A": hex(prime)
        })
        send_and_receive(sock, manipulated_payload)


        bob_response = send_and_receive(sock, "")
        manipulated_bob_response = json.dumps({"B": hex(prime)})
        send_and_receive(sock, manipulated_bob_response)


        encrypted_data = send_and_receive(sock, "")
        iv = encrypted_data['iv']
        encrypted_flag = encrypted_data['encrypted_flag']


        flag = decrypt_flag(iv, encrypted_flag)
        print(flag.decode(errors='ignore'))

perform_attack()
