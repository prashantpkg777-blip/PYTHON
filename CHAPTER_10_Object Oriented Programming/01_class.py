class Employee:
    language = "Python" # This is a class attribute
    salary = 120000

Pro = Employee()
Pro.name = "Prashant"
print(Pro.name,Pro.language,Pro.salary)

Dev = Employee()
Dev.name = "Devansh" # This is an instance attribute
print(Dev.name,Dev.language,Dev.salary)
Dev.salary = 130000
print(Dev.name,Dev.language,Dev.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
