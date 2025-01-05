import requests
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
res = bytes.fromhex(r.json()['ciphertext'])


print(f"Encrypted flag: {r.json()['ciphertext']}")


with open(r'C:\Users\caree\Desktop\crypto hack\Symmetric Cryptography\words.txt', 'r') as f:
    print("Starting brute force...")
    for word in f:
        word = word.strip()


        print(f"Trying password: {word}")


        key = hashlib.md5(word.encode()).digest()


        cipher = AES.new(key, AES.MODE_ECB)
        
        try: 
            decrypted = unpad(cipher.decrypt(res), AES.block_size)  
            
            
            if decrypted.startswith(b'crypto{'):
                print(f"Flag found: {decrypted.decode()}")
                print(f"Key (password): {word}")
                break
        except (ValueError, TypeError) as e:
            
            continue

print("Brute force completed.")
