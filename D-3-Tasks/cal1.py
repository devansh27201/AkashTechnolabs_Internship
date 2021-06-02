class cal1:
    def setdata(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
       
    def display(self):
       print ("Sum of numbers :",  n1+n2+n3)
n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))
c = cal1()

print(c.display())


