class Employee:
  a = 1

class Manager(Employee):
  b = 2

class SeniorManager(Manager):
  c = 3 

o = Employee()
print(o.a)

o1 = Manager()
print(o1.a, o1.b)

o2 = SeniorManager()
print(o2.a, o2.b, o2.c)