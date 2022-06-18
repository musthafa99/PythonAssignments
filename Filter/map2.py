n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
odd=list(filter(lambda n:n%2!=0,nums))

cube=list(map(lambda x:x*x*x,odd))


print(cube)
print(odd)
