class Person:
    def __init__(self,name,age,gender,city,state,mobile):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.state = state
        self.mobile = mobile

    def Details(self):
        print("Name of person:", self.name)
        print("Age of person:", self.age)
        print("Gender of person:", self.gender)
        print("City of person:", self.city)
        print("State of person:", self.state)
        print("Mobile number of person:", self.mobile)


person=Person('Ashok', 25, 'Male', 'Coimbatore', 'TamilNadu', 8056933435)
person.Details()
person1=Person("Sajina",27,"Female","Whitefield","Karnataka",8056723435)
person1.Details()