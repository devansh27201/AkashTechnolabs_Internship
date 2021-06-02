class publisher():
    def __init__(self):
        self.bookname = bookname
       
    def disp1(self):
        return f"Name of Book is  {self.bookname}"
      
class book(publisher):
    def __init__(self):
        publisher.__init__(self)
        self.pageno = no
    def disp2(self):
        return f"Number of pages in {self.bookname} are {self.pageno}"
class tape(publisher):
    def __init__(self):
        publisher.__init__(self)
        self.playtime = time
    def disp3(self):
        return f"Playtime of {self.bookname} book is {self.playtime}"
bookname = input("Enter Name of The Book : ")
no = int(input("Enter number of Pages : "))
time = int(input("Enter playtime of Book: "))        
p = publisher()
b = book()
t = tape()
print(p.disp1())
print(b.disp2())
print(t.disp3())
     