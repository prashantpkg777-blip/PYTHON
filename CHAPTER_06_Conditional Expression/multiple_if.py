a=int(input("Enter your age:"))

# If statement no: 1
if(a%2 == 0):
    print("age is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
  print("You are eligible.")
elif(a<0):
  print("Are mad!")  
  print("Please Enter your age in positive number.")
elif(a==0):
  print("You are entering 0 which is not a valid age")  
else:
  print("You are not eligible.") 
# End of If statement no: 2
