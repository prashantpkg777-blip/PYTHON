a=int(input("Enter your age:"))

# if elif else ladder
if(a>=18):
  print("You are eligible.")
elif(a<0):
  print("Are mad!")  
  print("Please Enter your age in positive number.")
elif(a==0):
  print("You are entering 0 which is not a valid age")  
else:
  print("You are not eligible.") 
   