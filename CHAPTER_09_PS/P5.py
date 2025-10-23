words = ["Donkey", "bad", "ganda"]

with open("donkey.txt", "r") as f:
    content = f.read()
    print(content)

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "a") as f:
    f.write(content)
    print(content)