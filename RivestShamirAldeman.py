## -------------------- Rivest Shamir Adleman -------------------- ##
#Written by: Aarni Junkkala

import random
import CarmichaelsTotientFunction as CTF
import RelativePrimenumbers as RP
import CongruenceRelation as CR

#Crypting system
# publickey = (n,e)
# privatekey = (n,d)
e = 0
d = 0
n = 0
def RSA(p,q):
    global e
    global n
    global d
    n = p * q
    a = CTF.CTF(n)
    CoPrimes = RP.FindRelativePrimenumbers(a)
    e = CoPrimes[random.randint(0,len(CoPrimes)-1)]
    ## ----- Finds d ----- ##
    d = 0
    num = 1
    while True:
        if CR.ConRel(1,e*num,a):
            d = num
            break
        num += 1
    
#     print("p: " + str(p))
#     print("q: " + str(q))
#     print("n: " + str(n))
#     print("a: " + str(a))
#     print("e: " + str(e))
#     print("d: " + str(d))
#     print("")
#     print("public key: " + str(n) + ", " + str(e))
#     print("private key: " + str(n) + ", " + str(d))

def encrypt(m,e,n): #m = message
    c = m ** e % n
    return c
    
def decrypt(c,d,n): #c= crypt
    m = c ** d % n
    return m

if __name__ == '__main__':
    RSA(61,53) #Must be primenumbers
    
    message = input("Input a message: ")
    
    crypted = []
    for i in range(len(message)):
        crypted.append(encrypt(ord(message[i]),e,n))
    print(crypted)
    decrypted = []
    for i in range(len(crypted)):
        decrypted.append(chr(decrypt(crypted[i],d,n)))
    print(decrypted)