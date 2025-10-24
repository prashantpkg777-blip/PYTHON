class Employee:
  salary = 234
  increment = 20

  @property
  def salaryAfterIncrement(self):
    return self.salary + (self.salary * self.increment / 100)

  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self, salary):
    self.increment = ((salary - self.salary) / self.salary) * 100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 275
print(e.increment)    