"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

#because a < b < c, a must be < 1000/3 

def f(n):
    for a in range(1, n//3):
        for b in range(a, n): # b > a
            c = n - b - a #calculate sum here instead of iterating c as well
            if (a**2 + b**2) == (c**2):
                return a * b * c
