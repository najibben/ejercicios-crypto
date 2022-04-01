import random

p = 941
g = 627
a =  347   
b =  781
A = ((pow(g, a)) % p)          
B = ((pow(g, b)) % p)
Ka = ((pow(B, a)) % p)
Kb = ((pow(A, b)) % p)
print("Secret key at A = ", str(Ka))
print("Secret key at B = ", str(Kb))