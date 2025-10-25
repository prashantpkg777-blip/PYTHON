# Mapping Example
l = [1, 2, 3, 4, 5]

square = lambda x: x * x
squared_list = list(map(square, l))
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# Filtering Example
def even(x):
    if (x % 2 == 0):
        return True
    return False

even_numbers = list(filter(even, l))
print(even_numbers)  # Output: [2, 4]

# Reducing Example
from functools import reduce
def add(x, y):
    return x + y

mul = lambda x, y: x * y

print(reduce(add, l))  # Output: 15
print(reduce(mul, l))  # Output: 120