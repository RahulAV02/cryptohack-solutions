def find_smallest_modulus():
    a = 11
    m1 = 6
    remainder1 = a - (a // m1) * m1  

    b = 8146798528947
    m2 = 17
    remainder2 = b - (b // m2) * m2   

    return remainder1 if remainder1 < remainder2 else remainder2

output = find_smallest_modulus()
print("The smallest remainder is:", output)
