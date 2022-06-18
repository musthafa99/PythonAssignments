n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
even=list(filter(lambda n:n%2==0,nums))

double=list(map(lambda x:x*2,even))


print(double)
print(even)
