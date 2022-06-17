from threading import *
import time
import threading
from threading import *
def cal_Square(num):
    for i in num:
        time.sleep(0.5)
        print("Square is:",i*i)
def cal_Cube(num):
    for i in num:
        time.sleep(0.7)
        print("Cube is:", i*i*i)
n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)

t1=threading.Thread(target=cal_Square,args=(numbers,))
t2=threading.Thread(target=cal_Cube,args=(numbers,))
t1.start()
t2.start()