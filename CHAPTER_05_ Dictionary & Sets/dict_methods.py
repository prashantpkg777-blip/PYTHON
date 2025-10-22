marks = {
  "Prashant": 100,
  "Nishant": 56,
  "Omi": 23,
  "Raju": 43
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Prashant":95,"Ashwani":35})
print(marks)

print(marks.get("Pro")) # Prints None
print(marks["Pro"]) # Returns an error