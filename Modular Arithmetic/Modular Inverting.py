def modular_inverse(a, p):
    return pow(a, p - 2, p)



result = modular_inverse(3, 13)
print(result)
