class Person():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year
    def welcome(self):
        print("Welcome",self.fname,self.lname,"to the class of",self.year)
x=Student("Anil","Rayudu",1995)
x.printname()