## -------------------- Relative primenumbers -------------------- ##
#Written by: Aarni Junkkala

import GreatestCommonDivisor as GCD
## ----- Gets the relative primes of the number ----- ##
def FindRelativePrimenumbers(n):
    num = 1
    CoPrimeNumbers = []
    while num <= n:
        if GCD.GCD([num,n]) == 1:
            CoPrimeNumbers.append(num)
        num += 1
    return CoPrimeNumbers