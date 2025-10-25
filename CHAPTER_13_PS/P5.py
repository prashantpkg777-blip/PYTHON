from functools import reduce

l = [6464, 234, 1234, 675, 3456, 9087, 12345, 9876]

def greater(a, b):
    if a > b:
        return a
    return b
largest = reduce(greater, l)
print("The largest number in the list is:", largest)
