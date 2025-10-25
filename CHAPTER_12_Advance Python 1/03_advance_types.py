from typing import List, Tuple, Dict, Union 

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5] 
print(numbers)

# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30)
print(person)

# Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 
print(scores)

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123"
print(identifier) 
identifier = 12345  # Also valid
print(identifier)