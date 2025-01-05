import binascii


hex_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

 
encrypted_bytes = binascii.unhexlify(hex_data)


for possible_key in range(256):
    
    decrypted_data = bytes([byte ^ possible_key for byte in encrypted_bytes])
    
     
    decoded_text = decrypted_data.decode('utf-8', errors='ignore')
    
     
    if " " in decoded_text and len(decoded_text) > 5:
        print(f"Key {possible_key} -> Decoded Message: {decoded_text}")
