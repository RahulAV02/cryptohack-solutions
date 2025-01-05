def check_primitive_root(candidate, prime_modulus):
    for exponent in range(2, prime_modulus):
        if pow(candidate, exponent, prime_modulus) == candidate:
            return False
    return True

prime_modulus = 28151
for possible_root in range(prime_modulus):
    if check_primitive_root(possible_root, prime_modulus):
        print(possible_root)
        break
