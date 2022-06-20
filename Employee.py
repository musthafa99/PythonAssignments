class Employee:
    def Details(self,name,age,Company_name,Gender):
        print("Name of Employee:",name)
        print("Age of Employee:", age)
        print("Employee Worked in:", Company_name)
        print("Gender of Employee:", Gender)

name=input()
age=int(input())
company=input()
gender=input()

employee=Employee()

employee.Details(name,age,company,gender)

