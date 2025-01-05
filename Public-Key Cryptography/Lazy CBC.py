import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def fetch_data(key_input):
    base_url = "http://aes.cryptohack.org/lazy_cbc/get_flag/"
    final_url = f"{base_url}{key_input.hex()}/"
    response = requests.get(final_url)
    content = response.json()
    return bytes.fromhex(content["plaintext"])

def get_invalid_response(cipher_text):
    base_url = "http://aes.cryptohack.org/lazy_cbc/receive/"
    full_url = f"{base_url}{cipher_text.hex()}/"
    response = requests.get(full_url)
    data = response.json()
    error_msg = data["error"]
    return bytes.fromhex(error_msg[len("Invalid plaintext: "):])

def xor_bytes(byte_seq1, byte_seq2):
    return long_to_bytes(bytes_to_long(byte_seq1) ^ bytes_to_long(byte_seq2))

dummy_block = b"\x00" * 32

invalid_output = get_invalid_response(dummy_block)
block_A = invalid_output[:16]
block_B = invalid_output[16:]

flag = fetch_data(xor_bytes(block_A, block_B))
print(flag)
