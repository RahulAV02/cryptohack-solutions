import requests
import binascii
from PIL import Image

base_url = 'http://aes.cryptohack.org/bean_counter/encrypt/'

def xor_bytes(byte_str1, byte_str2):
    return hex(int(byte_str1, 16) ^ int(byte_str2, 16))[2:].zfill(2)

def get_encrypted_data():
    response = requests.get(base_url)
    return response.json()['encrypted']

def save_decrypted_image(encrypted_msg, decryption_key):
    decrypted_hex = ''
    idx = 0
    for i in range(0, len(encrypted_msg), 2):
        decrypted_hex += xor_bytes(encrypted_msg[i:i+2], decryption_key[idx:idx+2])
        idx = (idx + 2) % len(decryption_key)
    
    decrypted_bytes = bytes.fromhex(decrypted_hex)
    with open('bean_counter.png', 'wb') as file:
        file.write(decrypted_bytes)

encrypted_data = get_encrypted_data()
encrypted_image = binascii.unhexlify(encrypted_data)
png_magic_number = '89504e470d0a1a0a0000000d49484452'

key_fragment = encrypted_data[:32]
decryption_key = ''

for i in range(0, len(key_fragment), 2):
    decryption_key += xor_bytes(key_fragment[i:i+2], png_magic_number[i:i+2])

save_decrypted_image(encrypted_data, decryption_key)

image = Image.open('bean_counter.png')
image.show()
