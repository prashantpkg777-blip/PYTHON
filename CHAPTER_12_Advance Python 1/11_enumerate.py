l = [3, 513, 53, 535]

index = 0
for item in l:
    print(f"At index {index} the value is {item}")
    index += 1
    
# Now using enumerate
print("Using enumerate now")    
for index, item in enumerate(l):
    print(f"At index {index} the value is {item}")