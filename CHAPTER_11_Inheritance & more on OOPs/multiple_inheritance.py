class Employee:
  company_name = "Tech Solutions"
  def show(self):
    print("Welcome to", self.company_name)

class coder:
  language = "Python"
  def coding_info(self):
    print("This coder writes code in", self.language)

class Developer(Employee, coder):
  company_name = "ITC"
  def developer_info(self):
    print(f"The name is {self.company_name} and the language is {self.language}.")

emp = Employee()
dev = Developer()    
dev.show()
dev.coding_info()
dev.developer_info()

print(emp.company_name, dev.company_name)