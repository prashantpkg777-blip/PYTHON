class Vector:
  def __init__(self, l):
    self.l = l

  def __len__(self):
    return len(self.l)  

v1 = Vector([1, 2, 3])
print("Length of v1 =", len(v1))
