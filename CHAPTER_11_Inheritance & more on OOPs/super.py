class Employee:
  def __init__(self):
    print("Constructor of Employee")
  a = 1

class Manager(Employee):
  def __init__(self):
    super().__init__()
    print("Constructor of Manager")
  b = 2

class SeniorManager(Manager):
  def __init__(self):
    super().__init__()
    print("Constructor of SeniorManager")
  c = 3

o = Employee()
print(o.a)

o1 = Manager()
print(o1.a, o1.b)

o2 = SeniorManager()
print(o2.a, o2.b, o2.c)