from Crypto.Util.number import inverse

a = 857504083339712752489993810777
b = 1029224947942998075080348647219
d = 65537

tot = (a-1) * (b-1)

print(inverse(d, tot))