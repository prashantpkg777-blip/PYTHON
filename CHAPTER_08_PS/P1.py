def greatest(a,b,c):
  if(a>b and a>c):
    return a
  elif(b>c and b>a):
    return b
  else:
    return c

a=5
b=6
c=7

print("The greatest number is",greatest(a,b,c))