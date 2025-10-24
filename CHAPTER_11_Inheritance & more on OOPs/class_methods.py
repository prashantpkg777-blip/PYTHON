class Employee:
  a = 1

  @classmethod
  def show(cls):
    print("This is a class method in Employee class. Value of a is:", cls.a)

e = Employee()
e.a = 10
e.show()
