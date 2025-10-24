class ComplexNumber:
    def __init__(self, real, imag):
        self.R = real
        self.I = imag

    def __add__(self, c2):
        return ComplexNumber(self.R + c2.R, self.I + c2.I)

    def __mul__(self, c2):
        real_part = (self.R * c2.R) - (self.I * c2.I)
        imag_part = (self.R * c2.I) + (self.I * c2.R)
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.R} + {self.I}i"    

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print("c1+c2 =", c1+c2)
print("c1*c2 =", c1*c2)