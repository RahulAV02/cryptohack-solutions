import json
import requests
from Crypto.Util.number import bytes_to_long, long_to_bytes


service_url = 'http://aes.cryptohack.org/flipping_cookie/'
default_config = 'admin=True;'


def fetch_cookie():
    response = requests.get(service_url + "get_cookie/")
    cookie_data = response.json()["cookie"]
    return cookie_data


def validate_admin(cookie, iv):
    response = requests.get(service_url + "check_admin/" + cookie + "/" + iv + "/")
    flag = response.json()["flag"]
    return flag


cookie = fetch_cookie()
iv_data = cookie[:32]
cipher_text = cookie[32:64]


expected_plaintext = b'admin=True;'
alternative_plaintext = b'admin=False'


iv_bytes = [int(iv_data[i:i+2], 16) for i in range(0, len(iv_data), 2)]


xor_result = []
for i in range(len(alternative_plaintext)):
    xor_result.append(alternative_plaintext[i] ^ expected_plaintext[i])


modified_iv = ''
for i in range(len(xor_result)):
    modified_iv += hex(xor_result[i] ^ iv_bytes[i])[2:].zfill(2)


if len(modified_iv) == len(xor_result) * 2:
    modified_iv += iv_data[len(modified_iv):]


if (bytes(xor_result).decode() == default_config and len(modified_iv) % 32 == 0):
    print(validate_admin(cookie[32:], modified_iv))
