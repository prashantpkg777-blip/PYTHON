n=int(input('Enter a number: '))

for i in range(2,n):
  if(n%2==0):
    print("Number is not Prime.")
    break
else:
  print("Number is Prime.")
