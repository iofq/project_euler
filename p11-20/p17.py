'''


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

digits = ("",
    "one ",
    "two ",
    "three ",
    "four ",
    "five ",
    "six ", 
    "seven ",
    "eight ",
    "nine ",
    "ten ",
    "eleven ",
    "twelve ",
    "thirteen ",
    "fourteen ",
    "fifteen ",
    "sixteen ",
    "seventeen ",
    "eighteen ",
    "nineteen ")

tens =("",
    "",
    "twenty ",
    "thirty ",
    "forty ",
    "fifty ",
    "sixty ",
    "seventy ",
    "eighty ",
    "ninety ")

def f(n):
    if n >= 1000:
        return digits[n // 1000] + "thousand " + f(n % 1000)
    if n >= 100:
        return digits[n // 100] + "hundred " + ("and " if n % 100 else "") + f(n % 100)
    if n >= 20:
        return tens[n // 10] + f(n % 10)
    return digits[n]

def iter(n=1000):
    return sum(len(f(i).replace(" ","")) for i in range(0,n + 1))
