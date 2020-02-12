#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

def gen_prime(n):
    P = [2]
    i = 3
    while len(P) < n:
        for p in P: #check against all previous primes
            if i % p == 0:
                break #stop looping on first factor
        #runs if break has not been reached
        else:
            P.append(i)
        i += 2 #skip all odd numbers
    return P[-1] #last index

