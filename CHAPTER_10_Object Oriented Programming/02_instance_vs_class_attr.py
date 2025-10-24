class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


pro = Employee()
pro.language = "JavaScript" # This is an instance attribute
print(pro.language, pro.salary)
