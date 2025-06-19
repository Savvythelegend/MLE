class Calculator:

    # let's add an intiliazer to the class  abs
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Calculator is ready to use")

    def add(self, a, b):
        return self.a + self.b
    
    def sub(self,a,b):
        return self.a - self.b

    def mul(self,a,b):
        return self.a * self.b
    
    def div(self,a,b):
        return self.a / self.b

    def mod(self,a,b):
        return self.a % self.b
    
a = Calculator(5,4)
val1 = a.add(2,3)
val2 = a.sub(5,4)
val3 = a.mul(5,4)
val4 = a.div(5,4)
val5 = a.mod(5,4)

print(f"Addition: {val1}\nSubtraction: {val2}\nMultiplication: {val3}\nDivision: {val4}\nModulus: {val5}")