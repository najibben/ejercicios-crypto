import libnum

import random
import sys

def getG(p):


  for x in range (1,p):
    rand = x
    exp=1
    next = rand % p

    while (next != 1 ):
        next = (next*rand) % p
        exp = exp+1
        

    if (exp==p-1):
        return rand

#M=583
p=1373

if (len(sys.argv)>1):
        M=int(sys.argv[1])
if (len(sys.argv)>2):
        p=int(sys.argv[2])

g=2

x=299
Y= pow(g,x,p)


k=877

#a=pow(g,k,p)
#b=(pow(Y,k,p)*M) %p
a=661
b=1325
'''
decryption
Algorithm 3
El gamal decryption algorithm
Decrypt a message (a,b) to find M
'''
m = (pow(a, p-1-x)*b)%p

message = (b * libnum.invmod(pow(a,x,p),p)) % p


print("\nBob Private key (x)=",x)
print("Bob picks g=",g)
print("Bob pick p=",p)
print("Bob computes Y=",Y)
print("Bob Public key (P,g,Y)=",p,g,Y)



#print("\nMessage=",M)
print("Alice select random k=",877)


print("\n\nCipher=",a,b)
print("\nDecrypt=",message)
print("\nDecrypt=",m)