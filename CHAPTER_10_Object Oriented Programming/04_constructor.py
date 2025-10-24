class Employee: 
    language = "Python" # This is a class attribute
    salary = 120000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Employee object is created")

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

pro = Employee("Prashant", 120000, "Python")
print(pro.name, pro.salary, pro.language)


pro.greet()
pro.get_info()            