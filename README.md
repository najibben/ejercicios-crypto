# ejercicios-crypto

Enunciados
# 1. (2 puntos) Alice y Bob quieren utilizar el intercambio de claves Diffie-Hellman para encontrar un secreto com´un del que derivar´an la clave secreta para un algoritmo sim´etrico.
Acuerdan utilizar el n´umero primo p = 941 y la ra´ız g = 627 como valores p´ublicos. Si Alice
toma como clave privada a = 347 y Bob toma como clave privada b = 781, ¿cu´al es el valor
secreto com´un?

```
Procfile: python3 DH.py

p=941
g=627
a=347
b=781

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


Secret key at A =  470
Secret key at B =  470
```
# 2. (3 puntos) Alice y Bob deciden utilizar el m´etodo de cifrado ElGamal para sus comunicaciones. Como valores p´ublicos toman p = 1373 y g = 2.

(i) Si Alice usa a = 947 como clave privada, ¿cu´al es su clave p´ublica A?

```
Procfile: elgamal.py

Y=gx(modp) = 177
Alice Public key (P,g,Y)= 1373 2 177
```

(ii) La clave privada de Bob es b = 716, ¿cu´al es su clave p´ublica B?

```
Procfile: elgamal.py
Bob Public key (P,g,Y)= 1373 2 469
```

(iii) Si Alice cifra el mensaje m = 583 usando la clave temporal k = 877, ¿cu´al es el mensaje
cifrado (c1, c2) que recibe Bob?

```
Procfile: elgamail.py
c1 = 719
c2 = 623
Bob Private key (x)= 716
Bob picks g= 2
Bob pick p= 1373
Bob computes Y= 469
Bob Public key (P,g,Y)= 1373 2 469

Message= 583
Alice select random k= 877


Cipher= 719 623

Decrypt= 583
```

(iv) Alice decide cambiar su clave privada por a = 299. Si Bob env´ıa a Alice el mensaje
cifrado (661, 1325), ¿pod´eis descifrar el mensaje?

```
Algorithm 3
El gamal decryption algorithm
Decrypt a message (r,t) to find M
1:
Calculate M = t × r−d mod p
m = (pow(a, p-1-x)*b)%p

Alice Private key (x)= 299
Alice picks g= 2
Alice pick p= 1373
Alice computes Y= 34
Alice Public key (P,g,Y)= 1373 2 34

Alice select random k= 877


Cipher= 661 1325

Decrypt= 332
```

# 3. (1 punto) Considerad la curva el´ıptica E : 
`y2 = x3+3x+5`, definida sobre `K = F19`. Calculad


el discriminante ∆(E), demostrad que el punto P = (4, 9) ∈ E(K) y calculad 2 · P.

# 4. (3 puntos) Alice y Bob usar´an la versi´on sobre curvas el´ıpticas del intercambio de claves
Diffie-Hellman utilizando el primo p = 2671, la curva E : y
2 = x
3 + 171x + 853 y el punto
P = (1980, 431) ∈ E(F2671).
(i) Si Alice env´ıa el punto QA = (2110, 543) y Bob usa la clave privada nB = 1943,
¿qu´e punto debe enviar Bob a Alice?

(ii) ¿Cu´al es el valor secreto com´un?

(iii) Alice y Bob deciden volver a ejecutar el algoritmo con los mismos valores p´ublicos, pero
ahora Alice s´olo env´ıa la coordenada xA = 2 de su punto QA. Bob ha cambiado su clave
secreta nB = 875. ¿Qu´e valor, modulo p, debe enviar Bob a Alice? ¿Cu´al es el valor
secreto com´un?

# 5. (1 punto) Sean E una curva el´ıptica sobre un cuerpo K y {P1, P2} una base de E[n].
Demostrad que el pairing de Weil, en(P1, P2), es una ra´ız n-´esima de la unidad. Observaci´on:
tened en cuenta que el pairing de Weil es no degenerado para acabar la demostraci´on.