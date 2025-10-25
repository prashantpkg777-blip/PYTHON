try:
  a=int(input("Enter a number: "))
  print(a)

except Exception as e:
  print("Some exception occurred")
  print(e)

else:
  print("No exception occurred")
  print("The number you entered is:", a)  