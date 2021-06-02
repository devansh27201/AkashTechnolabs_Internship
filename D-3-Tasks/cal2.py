class cal2:
    def setdata(self):
        self.r =int(input('Enter Radius: '))
    def area(self):
        self.a = self.r*self.r*3.14
    def display(self):
        print("Area of circle is: ",self.a)

c = cal2()
c.setdata()
c.area()
c.display()

