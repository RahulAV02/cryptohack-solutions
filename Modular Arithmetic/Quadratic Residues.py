def is_quadratic_residue(num, modulus):
    """Check if 'num' is a quadratic residue modulo 'modulus'."""
    for candidate in range(1, modulus):
        if (candidate * candidate) % modulus == num:
            return True, candidate
    return False, None

def get_square_root(num_list, modulus):
     
    for num in num_list:
        is_residue, root = is_quadratic_residue(num, modulus)
        if is_residue:
             
            negative_root = (modulus - root) % modulus
            return min(root, negative_root)
    return None

 
modulus = 29
numbers = [14, 6, 11]

 
result = get_square_root(numbers, modulus)

 
print("The flag (smaller square root) is:", result)
