import random
from pwn import *
from hashlib import md5
from json import dumps, loads
from sympy import nextprime
from Crypto.Util.number import bytes_to_long, long_to_bytes

def generate_input(): 
    input1 = [random.randint(0, 0xFFFFFFFF) for _ in range(16)]
    input2 = [x ^ (random.randint(0, 1 << 31) if i % 2 == 0 else 0) for i, x in enumerate(input1)]
    return bytes(input1), bytes(input2)

def get_prime_from_input(input_data): 
    prime_candidate = nextprime(256**2 * bytes_to_long(input_data))
    suffix = prime_candidate - 256**2 * bytes_to_long(input_data)
    return prime_candidate, suffix

def prepare_payload(prime, input_data, suffix): 
    input_with_suffix = input_data + b'\x00' + suffix.to_bytes(32, 'big')
    non_prime_value = bytes_to_long(input_with_suffix)
    return non_prime_value

def main():
    input1, input2 = generate_input()
    
    
    if md5(input1).hexdigest() == md5(input2).hexdigest():
        print("Hashes match!")
    else:
        print("Hashes do not match.")
        return

    prime, suffix = get_prime_from_input(input1)
    non_prime = prepare_payload(input2, suffix)

    print(f"Non-prime value: {non_prime}")


    r = remote("socket.cryptohack.org", 13392)
    sign_request = dumps({"option": "sign", "prime": prime}).encode()
    r.recvline()
    r.sendline(sign_request)

    sign_response = loads(r.recvline().decode())['signature']
    print(f"Received signature: {sign_response}")

    check_request = dumps({"option": "check", "prime": non_prime, "signature": sign_response, "a": 367}).encode()
    r.sendline(check_request)

    r.interactive()

if __name__ == "__main__":
    main()
