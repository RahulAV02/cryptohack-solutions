import binascii

 
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_KEYS_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


KEY1 = binascii.unhexlify(KEY1_hex)
KEY2_XOR_KEY1 = binascii.unhexlify(KEY2_XOR_KEY1_hex)
KEY2_XOR_KEY3 = binascii.unhexlify(KEY2_XOR_KEY3_hex)
FLAG_XOR_KEYS = binascii.unhexlify(FLAG_XOR_KEYS_hex)

 
KEY2 = bytes([a ^ b for a, b in zip(KEY2_XOR_KEY1, KEY1)])

 
KEY3 = bytes([a ^ b for a, b in zip(KEY2_XOR_KEY3, KEY2)])

 
flag = FLAG_XOR_KEYS
for key in [KEY1, KEY3, KEY2]:
    flag = bytes([a ^ b for a, b in zip(flag, key)])


print("Recovered flag:", flag.decode('utf-8'))
