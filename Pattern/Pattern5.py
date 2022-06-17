n=int(input())
for i in range(n):
    for j in range(n):
        if(i<j):
            print(chr(65+14+j),end=" ")
        else:
            print(chr(65+j), end=" ")
    print()