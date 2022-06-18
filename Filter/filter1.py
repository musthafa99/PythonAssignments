from functools import reduce

n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
even=list(filter(lambda n:n%2==0,nums))

double=list(map(lambda x:x*2,even))

sum=reduce(lambda a,b:a+b,double)
print(double)
print(even)
print(sum)