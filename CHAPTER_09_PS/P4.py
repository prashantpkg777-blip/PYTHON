word = "Donkey"

with open("donkey.txt","r") as f:
  content=f.read()

contentNew = content.replace(word,"Monkey")

with open("donkey.txt","w") as f:
  f.write(contentNew)
