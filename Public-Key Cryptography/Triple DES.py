import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def perform_encryption(secret_key, plaintext):
    base_url = "http://aes.cryptohack.org/triple_des/encrypt/"
    full_url = f"{base_url}{secret_key}/{plaintext.hex()}/"
    response = requests.get(full_url).json()
    return bytes.fromhex(response["ciphertext"])

def get_encrypted_flag(secret_key):
    base_url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    full_url = f"{base_url}{secret_key}/"
    response = requests.get(full_url).json()
    return bytes.fromhex(response["ciphertext"])

key_input = b'\x00' * 8 + b'\xff' * 8
encrypted_flag = get_encrypted_flag(key_input.hex())
cipher_text = perform_encryption(key_input.hex(), encrypted_flag)
print(cipher_text)
