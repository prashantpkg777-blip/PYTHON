print('Welcome to reverse table calculator.')
n = int(input('Enter your number: '))

for i in range(10,0,-1):
  print(f'{n} X {i} = {i*n}')