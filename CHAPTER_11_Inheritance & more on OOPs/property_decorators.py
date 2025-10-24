class Employee:
  a = 1

  @classmethod
  def show(cls):
    print("This is a class method in Employee class. Value of a is:", cls.a)

  @property
  def name(self):
    return f"{self.fname} {self.lname}"  

  @name.setter
  def name(self, value):
    self.fname, self.lname = value.split(" ")

e = Employee()
e.a = 10

e.name = "Prashant Kumar"
print(e.name)
print(e.fname, e.lname)

e.show()
