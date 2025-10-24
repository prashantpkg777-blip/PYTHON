class Number:
  def __init__(self, n):
    self.n = n

  def __add__(self, other):
    return self.n + other.n

  def __sub__(self, other):
    return self.n - other.n

  def __mul__(self, other):
    return self.n * other.n

  def __truediv__(self, other):
    return self.n / other.n

n = Number(5)
m = Number(10)

print("The sum is:", n + m)
print("The difference is:", n - m)
print("The product is:", n * m)
print("The division is:", n / m)