n= int(input('Enter a number: '))

product=1
for i in range(1,n+1):
  product =i*product

print(f"The factorial of {n} is {product}")  