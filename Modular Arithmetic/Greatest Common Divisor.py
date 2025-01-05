def calculate_gcd(num1, num2):
    
    while num2:  
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

if __name__ == "__main__":

    number1 = 66528
    number2 = 52920


    gcd_result = calculate_gcd(number1, number2)
    print(f"The GCD of {number1} and {number2} is: {gcd_result}")
