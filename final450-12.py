#cyclicallyrotatearray by 1
a = list(map(int,input().split()))

n = len(a)
last = a[n-1]   
for i in range(n-1,0,-1):
    a[i] = a[i-1];
a[0] = last;
    
for i in range(0,n):
    print(a[i],end = " ")
    
    
