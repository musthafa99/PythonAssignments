pos=-1
def Search(num,ele):
    left=0
    right=len(num)-1
    while left<=right:
        mid=(left+right)//2
        if num[mid]==ele:
            globals()['pos'] = mid
            return True
        elif num[mid]<ele:
            left=mid+1
        else:
            right=mid-1
    return False

n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)
print(numbers)
element=int(input())
numbers.sort()
if Search(numbers,element):
    print("Element is Found at",pos)
else:
    print("Element is Not Found")
