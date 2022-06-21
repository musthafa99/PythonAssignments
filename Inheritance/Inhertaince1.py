class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.year=year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class",self.year,"batch")

firstname=input()
lastname=input()
year=int(input())

x=Student("firstname","lastname",year)
x.welcome()