## -------------------- Carmichael's totient function -------------------- ##
#Written by: Aarni Junkkala

#Also known as:
    #reduced totient function
    #least universal exponent function
    #Usually uses symbol of greek letter Lambda (λ)

import CongruenceRelation as CR
import RelativePrimenumbers as RP
def CTF(n):
    ## ----- Gets the relative primes of the number ----- ##
    CoPrimeNumbers = RP.FindRelativePrimenumbers(n)
    
    ## ----- Finds the number ----- ##
    num = 1
    while True:
        found = True
        for i in range(len(CoPrimeNumbers)):
            if CR.ConRel(CoPrimeNumbers[i] ** num, 1, n) == False:
                found = False
                break
        if found == True:
            return num
        num += 1

## ----- Other names for the function ----- ##
def Lambda(n): #λ()
    return CTF(n)
def LUEF(n): #least universal exponent function
    return CTF(n)
def RTF(n):#reduced totient function
    return CTF(n)

if __name__ == '__main__':
    for i in range(1,36):
        print(str(i) + ", " + str(CTF(i)))