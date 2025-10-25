def divisble_by_5(n):
  if (n%5==0):
    return True
  return False

l = [10, 23, 45, 66, 89, 90, 34, 22, 55]
divisible = list(filter(divisble_by_5, l))
print(divisible)  