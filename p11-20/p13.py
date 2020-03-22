'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(see p13.txt)
'''

#read file to array, slice only first 11 digits
def read_file(f="p13.txt"):
    with open(f) as file:
        lines = [int(line.rstrip()[0:11]) for line in file]
    return lines

def main():
    n = read_file()
    sum = 0
    for i in n:
        sum += i
    return(str(sum)[0:10])

