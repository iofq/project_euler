#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(n):
    old = str(n)
    new = []
    length = len(old)
    for i in range(1, length+1): #first value will be length - 1, last will be 0
        new.append(old[length - i])
    return int(''.join(new))

def iter():
    largest = 0
    for i in range(999, 99, -1): #all 3 digit numbers reversed
        for j in range(999, 99, -1):
            t = i * j
            r = reverse(t)
            if r == t and t >= largest:
                largest = t
    return largest
                

