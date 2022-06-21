#Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Dog will Bark")
class DogChild(Dog):
    def eat(self):
        print("Eating Bread")

d=DogChild()
d.bark()
d.speak()
d.eat()
