"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import math

#Sieve of Eratosthenes implementation
def gen_primes(n=2000000):
    P = [True] * (n+1) #array of booleans to n, setting 0 and 1 manually to False
    P[0] = False       #loop will start at 2 and the rest will be calculated
    P[1] = False

    for i in range(2, math.ceil(n ** 0.5)):
        if P[i]:
            #for j = i^2, i^2 + i, i^2 + 2i, ... <=n
            j = i ** 2 
            while j <= n:
                P[j] = False
                j += i
    return f(P)
                
#sum index of true booleans
def f(P):
    sum = 0
    for i,p in enumerate(P):
        if p:
            sum += i
    return sum
