from functools import reduce

n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
odd=list(filter(lambda n:n%2!=0,nums))
sum=reduce(lambda a,b:a-b,odd)
print(odd)
print(sum)