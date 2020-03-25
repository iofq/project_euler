'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def main(x=20,y=20):
    return f(x+y) / (f(x) * f(y))

def f(n):
    return n if n == 1 else n * f(n-1)
