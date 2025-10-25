try:
  with open("1.txt") as f:
      a = f.read()
      print(a)
except Exception as e:
  print("Some exception occurred")
  print(e)

try:
  with open("2.txt") as f:
      b = f.read()
      print(b)
except Exception as e:
  print("Some exception occurred")
  print(e)

try:
  with open("3.txt") as f:
      c = f.read()
      print(c)
except Exception as e:
  print("Some exception occurred")
  print(e)  

print("The End")