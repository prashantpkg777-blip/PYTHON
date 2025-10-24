class Vector2D:
  def __init__(self, i, j):
    self.i = i
    self.j = j

  def show(self):
    print(f"The 2D vector is ({self.i}i, {self.j}j)") 

class Vector3D(Vector2D):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.k = k

  def show(self):
    print(f"The 3D vector is ({self.i}i, {self.j}j, {self.k}k)")

o = Vector2D(3, 4)
o.show()         

p = Vector3D(5, 6, 7)
p.show()