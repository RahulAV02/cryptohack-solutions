import binascii

 
encrypted_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"


encrypted_data = binascii.unhexlify(encrypted_hex)


flag_start = "flag{"
flag_end = "}"


for key in range(256):
    
    decrypted_bytes = bytes([byte ^ key for byte in encrypted_data])
    
    
    decoded_str = decrypted_bytes.decode('utf-8', errors='ignore')
    
    
    if decoded_str.startswith(flag_start) and decoded_str.endswith(flag_end):
        print(f"Found flag with key {key}: {decoded_str}")
        break
