def extended_gcd(a, b): 
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def chinese_remainder_theorem(congruences, moduli):
    result = 0
    total_product = 1
    for mod in moduli:
        total_product *= mod

    for ai, ni in zip(congruences, moduli):
         
        partial_product = total_product // ni
        
        gcd, inverse, _ = extended_gcd(partial_product, ni)
        if gcd != 1:
            raise ValueError(f"Moduli {ni} and {partial_product} are not coprime!")
         
        result += ai * partial_product * inverse

    return result % total_product

 
congruences = [2, 3, 5]   
moduli = [5, 11, 17]     

 
x = chinese_remainder_theorem(congruences, moduli)

print("Solution:", x)
