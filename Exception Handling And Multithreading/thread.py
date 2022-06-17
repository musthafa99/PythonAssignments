from threading import *
class A(Thread):
    def run(self):
        for i in range(6):
            print("Hello")



class B(Thread):
    def run(self):
        for i in range(6):
            print("Hi")

t1=A()
t2=B()

t1.start()
t2.start()