class calculator:
    def __init__(self, n):
      self.n = n
      print("Welcome to the calculator program")

    def square(self):
        print("The square of", self.n, "is", self.n ** 2)

    def cube(self):
        print("The cube of", self.n, "is", self.n ** 3)

    def squareroot(self):
        print("The square root of", self.n, "is", self.n ** 0.5)

n = int(input("Enter a number: "))
obj = calculator(n)

obj.square()
obj.cube()
obj.squareroot()
