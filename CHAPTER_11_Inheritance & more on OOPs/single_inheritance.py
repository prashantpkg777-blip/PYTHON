class Employee:
  company_name = "Tech Solutions"
  def show(self):
    print("Welcome to", self.company_name)

class Developer(Employee):
  company_name = "ITC"
  def developer_info(self):
    print("This is the Developer class inheriting from Employee class.")

emp = Employee()
dev = Developer()    
dev.show()
dev.developer_info()

print(emp.company_name, dev.company_name)