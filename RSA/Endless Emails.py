#!/usr/bin/env python3
from Crypto.Util import number
from itertools import combinations

def read_encrypted_data():
    """Reads the encrypted data from the file and returns n and c values."""
    data = {'n': [], 'c': []}
    with open("/content/output_0ef6d6343784e59e2f44f61d2d29896f.txt", 'rb') as file:
        for line in file:
            line = line.strip().decode()
            if line:
                key, value = line.split('=')
                key = key.strip()
                if key == 'e':
                    continue
                data[key].append(int(value))
    return data

def integer_root(value, root_degree):
    """Finds the integer part of the nth root of a number."""
    if value < 0 and root_degree % 2 == 0:
        raise ValueError("Cannot compute an even root of a negative number.")
    low, high = 0, value
    while low < high:
        mid = (low + high + 1) // 2
        if mid ** root_degree <= value:
            low = mid
        else:
            high = mid - 1
    return low

def perform_decryption(groups, exponent):
    """Performs decryption by applying Håstad’s Broadcast Attack using combinations."""
    for group in combinations(zip(groups['n'], groups['c']), exponent):
        modulus_product = 1
        for n, _ in group:
            modulus_product *= n
        
        cipher_sum = 0
        for n, c in group:
            partial_inverse = number.inverse(modulus_product // n, n)
            cipher_sum += c * partial_inverse * (modulus_product // n)
        cipher_sum %= modulus_product

         
        root = integer_root(cipher_sum, exponent)
        if root ** exponent == cipher_sum:
            print(number.long_to_bytes(root))


groups = read_encrypted_data()
perform_decryption(groups, 3)
