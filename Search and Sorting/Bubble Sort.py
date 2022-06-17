def bubblesort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp

n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)
print(numbers)
bubblesort(numbers)
print(numbers)