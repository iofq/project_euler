#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def f(n):
    i = 2
    while i <= n**0.5: #try to √n terms
        if n % i:
            i += 1
        else:
            n = n / i #if divisible, start from product
    return n #since we start from 2 and ++, n should be the largest
