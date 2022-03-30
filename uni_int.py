#union and intersection
m,n= map(int,input().split())

a = [5,6,1,2]
b = [1,2,3,4]

count = 0
#union - count = a+b
for i in range(0,m):
    for j in range(0,n):
        if a[i] == b[j]:
            count +=1 #count+=-1 union

print(count)
