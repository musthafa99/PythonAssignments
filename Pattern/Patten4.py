# print the pattern
# 1 2 3 4
# 2 3 4
# 3 4
# 4
n=int(input())
for i in range(0,n):
    x=i+1;
    for j in range(n-i):
        print(x,end=" ")
        x=x+1
    print()