class Employee: 
    language = "Python" # This is a class attribute
    salary = 120000

    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

pro = Employee()
pro.greet()
pro.get_info()            