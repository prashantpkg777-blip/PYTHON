'''
***
* *
*** 
n=3
'''
n=int(input('Enter a number: '))

for i in range(1,n+1):
  if(i==n or i==1):
    print("*" * n)
  else:
    print("*",end="")
    print(" " * (n-2),end="")
    print("*")