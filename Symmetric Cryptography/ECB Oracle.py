import requests
import time
import string

 
def send_encryption_request(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    response = requests.get(url + payload + '/')
    return response.json()['ciphertext']

 
def display_cipher_blocks(hex_data, block_size):
    for i in range(0, len(hex_data), block_size):
        print(hex_data[i:i+block_size], ' ', end='')
    print()

 
current_flag = ''
block_size = 32
alphabet_set = '_' + '@' + '{' + '}' + string.digits + string.ascii_lowercase + string.ascii_uppercase


while True:
    
    partial_payload = 'a' * (block_size - len(current_flag))
    expected_encryption = send_encryption_request(partial_payload.encode().hex())
    print('Encryption attempt:', '', end='')
    display_cipher_blocks(expected_encryption, block_size)

    for character in alphabet_set:
        full_payload = bytes.hex((partial_payload + current_flag + character).encode())
        encrypted_data = send_encryption_request(full_payload)
        print(character, '', end='')
        display_cipher_blocks(encrypted_data, block_size)
 
        if encrypted_data[32:64] == expected_encryption[32:64]:
            current_flag += character
            print(current_flag)
            break
        
        time.sleep(1)

    if current_flag.endswith('}'): 
        break

print(current_flag)
