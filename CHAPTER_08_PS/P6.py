def inches_to_cms(inch):
  return inch*2.54

n=int(input('Enter value in inches: '))

print(f"The value of {n} inches is {inches_to_cms(n)}cms")