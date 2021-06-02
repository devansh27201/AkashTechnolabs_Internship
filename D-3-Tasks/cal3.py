class cal3():
    def __init__(self):
        self.p = p
        self.r = r 
        self.t = t
    
    def calInterest(self):
        self.I = (p*r*t)/100
        
    def display(self):
         print("Simple Interest is : ",self.I)

p = float(input("Enter princial amount: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Amount of time: "))

c = cal3()
c.calInterest()
c.display()