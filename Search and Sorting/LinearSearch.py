pos=-1
def Search(num,ele):
    for i in range(len(num)):
        if num[i]==ele:
            globals()['pos'] = i
            return True
    return False

n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)
print(numbers)
element=int(input())

if Search(numbers,element):
    print("Element is Found at",pos)
else:
    print("Element is Not Found")



