try:
  a = int(input("Enter a number: "))
  print(a)

except ValueError as v:
  print("Hey")
  print(v)

except Exception as e:
  print("Some other exception")
  print(e)

print("The End")    