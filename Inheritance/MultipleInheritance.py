class Calculation1:
    def sum(self,a,b):
        return a+b

class Calculation2:
    def Multiplication(self,a,b):
        return a*b

class Calculation3(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b

x=int(input())
y=int(input())
result=Calculation3()
print(result.sum(x,y))
print(result.Multiplication(x,y))
print(result.Divide(x,y))