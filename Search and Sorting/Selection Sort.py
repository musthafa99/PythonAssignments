def Selectionsort(numbers):
    for i in range(len(numbers)):
        min = i
        for j in range(i + 1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j

        temp = numbers[i]
        numbers[i] = numbers[min]
        numbers[min] = temp


n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)
print(numbers)
Selectionsort(numbers)
print(numbers)
