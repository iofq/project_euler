#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

check = [20, 19, 18, 17, 16, 14, 13, 11] #do not check redundant numbers
#eg. checking for 20 also checks for 2, 4, 5, 10

def f(n):
    for i in check:
        if n % i:
            return False
    return True

def iter():
    i = 2520 #it won't be smaller than this
    smallest = 0

    while(smallest == 0):
        if(f(i)):
            return i
        else:
            i += 2520 #must be divisible by 2520, as 1,10 is a subset of 1,20 
    return -1
