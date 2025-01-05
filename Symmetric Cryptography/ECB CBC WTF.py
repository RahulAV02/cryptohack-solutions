import requests
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long

def fetch_decrypted_block(byte_data):
    api_url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    api_url += byte_data.hex() + "/"
    response = requests.get(api_url)
    data = response.json()
    return bytes.fromhex(data["plaintext"])

def retrieve_encrypted_flag():
    api_url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    response = requests.get(api_url)
    data = response.json()
    return bytes.fromhex(data["ciphertext"])

def xor_byte_strings(byte1, byte2):
    return long_to_bytes(bytes_to_long(byte1) ^ bytes_to_long(byte2))

encrypted_data = retrieve_encrypted_flag()

initialization_vector = encrypted_data[:16]
first_block = encrypted_data[16:32]
second_block = encrypted_data[32:]

decrypted_first_block = xor_byte_strings(fetch_decrypted_block(first_block), initialization_vector)
decrypted_second_block = xor_byte_strings(fetch_decrypted_block(second_block), first_block)

print(decrypted_first_block + decrypted_second_block)
