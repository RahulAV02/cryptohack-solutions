import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

api_url = 'http://aes.cryptohack.org/symmetry/'

def fetch_encrypted_flag():
    response = requests.get(f'{api_url}encrypt_flag/')
    encrypted_data = response.json()['ciphertext']
    return encrypted_data

def custom_encryption_request(plaintext, iv):
    response = requests.get(f'{api_url}encrypt/{plaintext}/{iv}/')
    encrypted_text = response.json()['ciphertext']
    return encrypted_text

encrypted_flag = fetch_encrypted_flag()
iv = encrypted_flag[:32]
ciphertext = encrypted_flag[32:]

encrypted_response = custom_encryption_request(ciphertext, iv)

cipher = AES.new(bytes.fromhex(iv), AES.MODE_CBC, iv=bytes.fromhex(iv))
decrypted_flag = unpad(cipher.decrypt(bytes.fromhex(encrypted_response)), AES.block_size)

print(decrypted_flag.decode())
