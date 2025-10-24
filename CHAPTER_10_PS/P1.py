class Programmer:
    company = "Microsoft" 
    salary = 150000
    pin = 560103

    def __init__(self, name, salary, company, pin):
        self.name = name
        self.salary = salary
        self.company = company
        self.pin = pin
        print("Here is the programmer details:")

p = Programmer("Prashant", 150000, "Microsoft", 560103)
print(p.name, p.salary, p.company, p.pin)

n = Programmer("Neha", 140000, "Google", 560104)
print(n.name, n.salary, n.company, n.pin)