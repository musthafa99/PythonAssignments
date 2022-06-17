from array import *

n=int(input())
num=array('i',[])
for j in range(n):
    value=int(input())
    num.append(value)
num.reverse()
print(num)
