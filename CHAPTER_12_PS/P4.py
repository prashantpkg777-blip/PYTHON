try:
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  print("The division of the two numbers is:", a / b)
except ZeroDivisionError as e:
  print("Infinite")
  