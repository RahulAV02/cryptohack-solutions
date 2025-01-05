import requests


response = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
encrypted_flag = response.json().get('ciphertext')


decryption_url = f'http://aes.cryptohack.org/block_cipher_starter/decrypt/{encrypted_flag}'
decryption_response = requests.get(decryption_url)


decrypted_flag_hex = decryption_response.json().get('plaintext')


decrypted_bytes = bytes.fromhex(decrypted_flag_hex)
decrypted_flag = decrypted_bytes.decode()


print(decrypted_flag)
