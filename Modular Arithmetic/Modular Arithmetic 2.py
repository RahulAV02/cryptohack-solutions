def modular_arithmetic():
    
    p1 = 17
    mod1 = pow(3, 17, p1)  
    mod2 = pow(5, 17, p1)   
    mod3 = pow(7, 16, p1)   

     
    p2 = 65537
    base = 273246787654
    exponent = 65536
    large_mod = pow(base, exponent, p2)

    return mod1, mod2, mod3, large_mod



results = modular_arithmetic()
print("3^17 mod 17:", results[0])
print("5^17 mod 17:", results[1])
print("7^16 mod 17:", results[2])
print("273246787654^65536 mod 65537:", results[3])
