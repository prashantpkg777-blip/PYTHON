myList = [1,2,5,9,34,50]

squaredList = []
for item in myList:
    squaredList.append(item**2)
print(squaredList)

# Using List Comprehension
squaredListComp = [item**2 for item in myList]
print(squaredListComp)