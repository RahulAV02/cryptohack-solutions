from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util import number
import math

data = {'moduli': [], 'ciphertexts': [], 'exponents': []}

for idx in range(1, 51):
    with open(f"keys_and_messages/{idx}.pem", 'r') as f:
        rsa_key = RSA.importKey(f.read())
    with open(f"keys_and_messages/{idx}.ciphertext", 'r') as f:
        ciphertext = int.from_bytes(bytes.fromhex(f.read()), "big")
    data['moduli'].append(rsa_key.n)
    data['ciphertexts'].append(ciphertext)
    data['exponents'].append(rsa_key.e)

common_mod = 0
for a in range(len(data['moduli'])):
    for b in range(a + 1, len(data['moduli'])):
        shared_factor = math.gcd(data['moduli'][a], data['moduli'][b])
        if shared_factor != 1:
            common_mod = shared_factor
            idx = a
            break
    if common_mod:
        break

if not common_mod:
    exit()

private_exponent = number.inverse(data['exponents'][idx], (common_mod - 1) * (data['moduli'][idx] // common_mod - 1))
rsa_key = RSA.construct((data['moduli'][idx], data['exponents'][idx], private_exponent))
decryptor = PKCS1_OAEP.new(rsa_key)
decrypted_message = decryptor.decrypt(number.long_to_bytes(data['ciphertexts'][idx]))

print(decrypted_message.decode())
