class cal4:
    def setdata(self,n1):
        self.n1 = n1
    def display(self):
       return n1*n1
n1 = int(input("Enter number: "))
c = cal4()

print(c.display())