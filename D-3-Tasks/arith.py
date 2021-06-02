class arith():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def addition(self):
        return self.n1+self.n2
    def subtraction(self):
        return self.n1-self.n2
    def multiplication(self):
        return self.n1*self.n2
    
        
n1 = int(input("Enter a Number: "))
n2 = int(input("Enter another Number: "))
a = arith(n1,n2)

print("Sum of both numbers is: ", a.addition())
print("Subtration of both numbers is: ", a.subtraction())
print("Multiplication of both numbers is: ", a.multiplication())



        